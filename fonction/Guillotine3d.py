"""
Fichier fait par Mathis
"""
from fonction.decorator import *
from module.marchandise import Marchandise
from module.conteneur import Conteneur
from module.train import Train

# ==> Mathis
class EspaceLibre3d:
    def __init__(self, x, y,z, longueur, largeur,hauteur):
        self.x = x
        self.y = y
        self.z = z
        self.longueur = longueur
        self.largeur = largeur
        self.hauteur = hauteur

    def getVolume(self):
        return self.longueur * self.largeur * self.hauteur

# === >Mathis
def obtenir_rotations(m : Marchandise):
    """Retourne les 6 permutations (longueur, largeur, hauteur) possibles pour une marchandise
    Si la marchandise est retournable"""
    perms=[]
    if m.retournable == 1:
        perms = [
            (m.longueur, m.largeur, m.hauteur),
            (m.longueur, m.hauteur, m.largeur),
            (m.largeur, m.longueur, m.hauteur),
            (m.largeur, m.hauteur, m.longueur),
            (m.hauteur, m.longueur, m.largeur),
            (m.hauteur, m.largeur, m.longueur)
        ]
    else :
        perms = [(m.longueur, m.largeur, m.hauteur),
                ( m.largeur,m.longueur, m.hauteur)]
    # On supprime les doublons (si la boîte est un cube parfait par exemple)
    return list(set(perms))

#==> Mathis
def splitheuristique(espace : EspaceLibre3d, marchandise : Marchandise):
    variations = []

    # --- Variation 1 : Z-Dominant (Le 'Dessus' prend toute la surface possible) ---
    v1_dessus = EspaceLibre3d(espace.x, espace.y, espace.z + marchandise.hauteur, espace.longueur, espace.largeur,
                              espace.hauteur - marchandise.hauteur)
    v1_droite = EspaceLibre3d(espace.x + marchandise.longueur, espace.y, espace.z,
                              espace.longueur - marchandise.longueur, marchandise.largeur, marchandise.hauteur)
    v1_derriere = EspaceLibre3d(espace.x, espace.y + marchandise.largeur, espace.z, espace.longueur,
                                espace.largeur - marchandise.largeur, marchandise.hauteur)
    variations.append([v1_dessus, v1_droite, v1_derriere])

    # --- Variation 2 : X-Dominant (La 'Droite' prend toute la hauteur et profondeur) ---
    v2_droite = EspaceLibre3d(espace.x + marchandise.longueur, espace.y, espace.z,
                              espace.longueur - marchandise.longueur, espace.largeur, espace.hauteur)
    v2_derriere = EspaceLibre3d(espace.x, espace.y + marchandise.largeur, espace.z, marchandise.longueur,
                                espace.largeur - marchandise.largeur, espace.hauteur)
    v2_dessus = EspaceLibre3d(espace.x, espace.y, espace.z + marchandise.hauteur, marchandise.longueur,
                              marchandise.largeur, espace.hauteur - marchandise.hauteur)
    variations.append([v2_droite, v2_derriere, v2_dessus])

    # --- Variation 3 : Y-Dominant (Le 'Derrière' prend toute la hauteur et largeur) ---
    v3_derriere = EspaceLibre3d(espace.x, espace.y + marchandise.largeur, espace.z, espace.longueur,
                                espace.largeur - marchandise.largeur, espace.hauteur)
    v3_droite = EspaceLibre3d(espace.x + marchandise.longueur, espace.y, espace.z,
                              espace.longueur - marchandise.longueur, marchandise.largeur, espace.hauteur)
    v3_dessus = EspaceLibre3d(espace.x, espace.y, espace.z + marchandise.hauteur, marchandise.longueur,
                              marchandise.largeur, espace.hauteur - marchandise.hauteur)
    variations.append([v3_derriere, v3_droite, v3_dessus])

    # --- Évaluation de la Heuristique ---
    meilleure_variation = None
    max_volume_trouve = -1

    for variation in variations:
        # On cherche le volume du plus gros bloc généré par cette variation
        plus_gros_bloc = max(variation, key=lambda e: e.getVolume()).getVolume()

        if plus_gros_bloc > max_volume_trouve:
            max_volume_trouve = plus_gros_bloc
            meilleure_variation = variation

    # On ne retourne que les espaces qui ont une taille réelle (volume > 0)
    espaces_valides = [e for e in meilleure_variation if e.longueur > 0 and e.largeur > 0 and e.hauteur > 0]

    return espaces_valides

#==> Mathis
def guillotine3d_opti(marchandises_triees):
    train = Train()
    # Dictionnaire pour lier un conteneur à sa liste d'espaces libres
    espaces_libres = {}


    for marchandise in marchandises_triees:
        place = False
        meilleur_espace = None
        meilleur_conteneur = None
        meilleur_indice = -1
        meilleur_volume = float('inf')
        meilleure_orientation = None
        rotation = obtenir_rotations(marchandise)
        # Chercher dans les conteneurs existants
        for conteneur in train.conteneurs:
            # Chercher le premier espace où ça rentre
            for i,espace in enumerate(espaces_libres[conteneur]):
                # Vérifier si ça rentre
                for r_long,r_large,r_haut in rotation:
                    if espace.longueur >= r_long and espace.largeur >= r_large and espace.hauteur >= r_haut:                        # la marchandise entre dans l'espace libre
                        #conteneur.contenu.append(marchandise)
                        #on stocke meilleur volume dés le début pour la comparaison
                        if espace.getVolume() < meilleur_volume:
                            meilleur_volume = espace.getVolume()
                            meilleur_espace = espace
                            meilleur_conteneur = conteneur
                            meilleur_indice = i
                            meilleure_orientation = (r_long, r_large, r_haut)
                        place = True
        if place:
            marchandise.x=meilleur_espace.x
            marchandise.y=meilleur_espace.y
            marchandise.z=meilleur_espace.z


            espaces_libres[meilleur_conteneur].pop(meilleur_indice)
            meilleur_conteneur.contenu.append(marchandise)
            marchandise.longueur, marchandise.largeur, marchandise.hauteur = meilleure_orientation

            espaceopti = splitheuristique(meilleur_espace, marchandise)
            espaces_libres[meilleur_conteneur].extend(espaceopti)
        # Si aucun espace trouvé, on ouvre un nouveau conteneur
        else:
            nouveau_conteneur = Conteneur()
            train.conteneurs.append(nouveau_conteneur)

            # L'espace libre initial = tout le conteneur
            espace_initial = EspaceLibre3d(0, 0,0, nouveau_conteneur.longueur, nouveau_conteneur.largeur,nouveau_conteneur.hauteur)
            espaces_libres[nouveau_conteneur] = [espace_initial]

            # On place l'objet dans ce nouveau conteneur
            nouveau_conteneur.contenu.append(marchandise)

            espaceopti = splitheuristique(espace_initial, marchandise)
            espaces_libres[nouveau_conteneur].extend(espaceopti)
            espaces_libres[nouveau_conteneur].pop(0)


    return train


@chronometrer
def guillotine3dOffline_opti(marchandises_obj):
    """
    :param marchandises_obj: list(Marchandise)
    :return: Train()
    """
    # Tri hors-ligne (Offline) : Du plus grand au plus petit (très important pour Guillotine)
    # On utilise ta méthode getSurface()
    marchandises_triees = marchandises_obj.all
    #rail=marchandises_triees[5]
    marchandises_triees = sorted(
        marchandises_obj.all,
        key=lambda m: (max(m.longueur, m.largeur, m.hauteur), m.getVolume()),
        reverse=True
    )    #marchandises_triees.insert(0, rail)
    #print(marchandises_triees.index(rail))
    return guillotine3d_opti(marchandises_triees)

@chronometrer
def guillotine3dOnline_opti(marchandises_obj):
    """
        :param marchandises_obj: list(Marchandise)
        :return: Train()
        """
    # Tri en ligne (Online)
    marchandises_triees = marchandises_obj.all
    return guillotine3d_opti(marchandises_triees)


def guillotine3d(marchandises_triees):
    train = Train()
    # Dictionnaire pour lier un conteneur à sa liste d'espaces libres
    espaces_libres = {}
    for marchandise in marchandises_triees:
        place = False
        # Chercher dans les conteneurs existants
        for conteneur in train.conteneurs:
            # Chercher le premier espace où ça rentre
            for i,espace in enumerate(espaces_libres[conteneur]):
                # Vérifier si ça rentre
                if espace.longueur >= marchandise.longueur and espace.largeur >= marchandise.largeur and espace.hauteur >= marchandise.hauteur:
                    # Ajouter au conteneur
                    conteneur.contenu.append(marchandise)

                    # Coupe Guillotine
                    # Création des deux nouveaux espaces libres restants
                    espace_droit = EspaceLibre3d(
                        x=espace.x + marchandise.longueur,
                        y=espace.y,
                        z=espace.z,
                        longueur=espace.longueur - marchandise.longueur,
                        largeur=marchandise.largeur,
                        hauteur= marchandise.hauteur
                    )

                    espace_derriere = EspaceLibre3d(
                        x=espace.x,
                        y=espace.y + marchandise.largeur,
                        z=espace.z,
                        longueur=espace.longueur,
                        largeur=espace.largeur - marchandise.largeur,
                        hauteur=marchandise.hauteur
                    )

                    espace_dessus = EspaceLibre3d(
                        x=espace.x,
                        y=espace.y ,
                        z=espace.z + marchandise.hauteur,
                        longueur=espace.longueur,
                        largeur=espace.largeur,
                        hauteur=espace.hauteur-marchandise.hauteur
                    )

                    #Remplacer l'ancien espace par les deux nouveaux (s'ils ne sont pas vides)
                    espaces_libres[conteneur].pop(i)

                    if espace_droit.longueur > 0 and espace_droit.largeur > 0 and espace_droit.hauteur > 0:
                        espaces_libres[conteneur].append(espace_droit)
                    if espace_dessus.longueur > 0 and espace_dessus.largeur > 0 and espace_dessus.hauteur > 0:
                        espaces_libres[conteneur].append(espace_dessus)
                    if espace_derriere.longueur > 0 and espace_derriere.largeur > 0 and espace_derriere.hauteur > 0:
                        espaces_libres[conteneur].append(espace_derriere)

                    place = True
                    break
            if place:
                break  # On passe à la marchandise suivante
        # Si aucun espace trouvé, on ouvre un nouveau conteneur
        if not place:
            nouveau_conteneur = Conteneur()
            train.conteneurs.append(nouveau_conteneur)

            # L'espace libre initial = tout le conteneur
            espace_initial = EspaceLibre3d(0, 0,0, nouveau_conteneur.longueur, nouveau_conteneur.largeur,nouveau_conteneur.hauteur)
            espaces_libres[nouveau_conteneur] = [espace_initial]

            # On place l'objet dans ce nouveau conteneur
            nouveau_conteneur.contenu.append(marchandise)

            #On divise l'espace en 3 autres parallépipède comme dans la partie précédente

            espace_droit = EspaceLibre3d(x =marchandise.longueur,
                                         y = 0,
                                         z = 0,
                                         longueur = nouveau_conteneur.longueur - marchandise.longueur,
                                         largeur = marchandise.largeur,
                                         hauteur = marchandise.hauteur)
            espace_dessus = EspaceLibre3d(x =0,
                                         y = 0,
                                         z = marchandise.hauteur,
                                         longueur = nouveau_conteneur.longueur,
                                         largeur = nouveau_conteneur.largeur,
                                         hauteur = nouveau_conteneur.hauteur - marchandise.hauteur)

            espace_derriere = EspaceLibre3d(x=0,
                                         y=marchandise.largeur,
                                         z=0,
                                         longueur=nouveau_conteneur.longueur,
                                         largeur=nouveau_conteneur.largeur - marchandise.largeur,
                                         hauteur=marchandise.hauteur)

            espaces_libres[nouveau_conteneur].pop(0)
            if espace_droit.longueur > 0: espaces_libres[nouveau_conteneur].append(espace_droit)
            if espace_derriere.largeur > 0: espaces_libres[nouveau_conteneur].append(espace_derriere)
            if espace_dessus.hauteur > 0: espaces_libres[nouveau_conteneur].append(espace_dessus)


    return train

@chronometrer
def guillotine3dOffline(marchandises_obj):
    """

    :param marchandises_obj:
    :return: Train()
    Le guillotine sans optimisation de base pour le 3d en l'adaptant depuis le 2d
    """
    # Tri hors-ligne (Offline) : Du plus grand au plus petit (très important pour Guillotine)
    # On utilise ta méthode getSurface()

    marchandises_triees = sorted(marchandises_obj.all, key=lambda m: m.hauteur, reverse=True)

    return guillotine3d(marchandises_triees)

@chronometrer
def guillotine3dOnline(marchandises_obj):
    marchandises_triees = marchandises_obj.all
    return guillotine3d(marchandises_triees)


