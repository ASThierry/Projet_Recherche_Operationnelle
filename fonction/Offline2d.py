from fonction.decorator import *
from module.marchandise import Marchandise
from module.conteneur import Conteneur
from module.train import Train

# Structure pour traquer les espaces vides
class EspaceLibre:
    def __init__(self, x, y, longueur, largeur):
        self.x = x
        self.y = y
        self.longueur = longueur
        self.largeur = largeur

    def contient(self, autre_espace):
        """Vérifie si cet espace englobe totalement un autre espace."""
        return (self.x <= autre_espace.x and
                self.y <= autre_espace.y and
                self.x + self.longueur >= autre_espace.x + autre_espace.longueur and
                self.y + self.largeur >= autre_espace.y + autre_espace.largeur)

@chronometrer
def guillotine2dOffline(marchandises_obj):
    train = Train()
    # Dictionnaire pour lier un conteneur à sa liste d'espaces libres
    espaces_libres = {}

    # Tri hors-ligne (Offline) : Du plus grand au plus petit (très important pour Guillotine)
    # On utilise ta méthode getSurface()
    marchandises_triees = sorted(marchandises_obj.all, key=lambda m: m.largeur, reverse=True)

    for marchandise in marchandises_triees:
        place = False

        # Chercher dans les conteneurs existants
        for conteneur in train.conteneurs:
            # Chercher le premier espace où ça rentre (First Fit)
            for i, espace in enumerate(espaces_libres[conteneur]):
                # Vérifier si ça rentre
                if espace.longueur >= marchandise.longueur and espace.largeur >= marchandise.largeur:

                    # Ajouter au conteneur
                    conteneur.contenu.append(marchandise)

                    # Coupe Guillotine
                    # Création des deux nouveaux espaces libres restants
                    espace_droit = EspaceLibre(
                        x=espace.x + marchandise.longueur,
                        y=espace.y,
                        longueur=espace.longueur - marchandise.longueur,
                        largeur=marchandise.largeur
                    )

                    espace_haut = EspaceLibre(
                        x=espace.x,
                        y=espace.y + marchandise.largeur,
                        longueur=espace.longueur,
                        largeur=espace.largeur - marchandise.largeur
                    )

                    #Remplacer l'ancien espace par les deux nouveaux (s'ils ne sont pas vides)
                    espaces_libres[conteneur].pop(i)
                    if espace_droit.longueur > 0 and espace_droit.largeur > 0:
                        espaces_libres[conteneur].append(espace_droit)
                    if espace_haut.longueur > 0 and espace_haut.largeur > 0:
                        espaces_libres[conteneur].append(espace_haut)

                    place = True
                    break

            if place:
                break # On passe à la marchandise suivante

        # Si aucun espace trouvé, on ouvre un nouveau conteneur
        if not place:
            nouveau_conteneur = Conteneur()
            train.conteneurs.append(nouveau_conteneur)

            # L'espace libre initial = tout le conteneur
            espace_initial = EspaceLibre(0, 0, nouveau_conteneur.longueur, nouveau_conteneur.largeur)
            espaces_libres[nouveau_conteneur] = [espace_initial]

            # On place l'objet dans ce nouveau conteneur (répétition de la coupe)
            nouveau_conteneur.contenu.append(marchandise)

            espace_droit = EspaceLibre(marchandise.longueur,
                                       0,
                                       nouveau_conteneur.longueur - marchandise.longueur,
                                       marchandise.largeur)
            espace_haut = EspaceLibre(0,
                                      marchandise.largeur,
                                      nouveau_conteneur.longueur,
                                      nouveau_conteneur.largeur - marchandise.largeur)

            espaces_libres[nouveau_conteneur].pop(0)
            if espace_droit.longueur > 0: espaces_libres[nouveau_conteneur].append(espace_droit)
            if espace_haut.largeur > 0: espaces_libres[nouveau_conteneur].append(espace_haut)

    return train


def diviser_espace(espace, marchandise):
    """
    Si la marchandise chevauche l'espace, divise l'espace en 4 nouveaux
    espaces potentiels (qui représentent le vide autour de la marchandise).
    """
    nouveaux_espaces = []

    # Vérifier si la marchandise intersecte l'espace libre
    intersecte = (marchandise.x < espace.x + espace.longueur and
                  marchandise.x + marchandise.longueur > espace.x and
                  marchandise.y < espace.y + espace.largeur and
                  marchandise.y + marchandise.largeur > espace.y)

    if not intersecte:
        return [espace] # Pas d'intersection, on rend l'espace tel quel

    # 1. Espace à GAUCHE de la marchandise
    if marchandise.x > espace.x:
        nouveaux_espaces.append(EspaceLibre(
            espace.x, espace.y,
            marchandise.x - espace.x, espace.largeur
        ))

    # 2. Espace à DROITE de la marchandise
    if marchandise.x + marchandise.longueur < espace.x + espace.longueur:
        nouveaux_espaces.append(EspaceLibre(
            marchandise.x + marchandise.longueur, espace.y,
            (espace.x + espace.longueur) - (marchandise.x + marchandise.longueur), espace.largeur
        ))

    # 3. Espace en BAS de la marchandise
    if marchandise.y > espace.y:
        nouveaux_espaces.append(EspaceLibre(
            espace.x, espace.y,
            espace.longueur, marchandise.y - espace.y
        ))

    # 4. Espace en HAUT de la marchandise
    if marchandise.y + marchandise.largeur < espace.y + espace.largeur:
        nouveaux_espaces.append(EspaceLibre(
            espace.x, marchandise.y + marchandise.largeur,
            espace.longueur, (espace.y + espace.largeur) - (marchandise.y + marchandise.largeur)
        ))

    return nouveaux_espaces

@chronometrer
def maxrects2dOffline(marchandises_obj):
    train = Train()
    espaces_libres_par_conteneur = {}

    # Tri Offline : Toujours du plus grand au plus petit (très important)
    marchandises_triees = sorted(marchandises_obj.all, key=lambda m: m.getSurface(), reverse=True)

    for marchandise in marchandises_triees:
        meilleur_conteneur = None
        meilleur_espace = None
        meilleur_score = float('inf')  # Le plus petit score (reste de surface) gagne

        # 1. Chercher le meilleur emplacement parmi tous les conteneurs ouverts
        for conteneur in train.conteneurs:
            for espace in espaces_libres_par_conteneur[conteneur]:
                if espace.longueur >= marchandise.longueur and espace.largeur >= marchandise.largeur:
                    # Calculer l'aire restante si on place la marchandise ici (Best Area Fit)
                    surface_restante = (espace.longueur * espace.largeur) - marchandise.getSurface()
                    if surface_restante < meilleur_score:
                        meilleur_score = surface_restante
                        meilleur_espace = espace
                        meilleur_conteneur = conteneur

        # 2. Si aucun espace trouvé, ouvrir un nouveau conteneur
        if meilleur_conteneur is None:
            meilleur_conteneur = Conteneur()
            train.conteneurs.append(meilleur_conteneur)
            espace_initial = EspaceLibre(0, 0, meilleur_conteneur.longueur, meilleur_conteneur.largeur)
            espaces_libres_par_conteneur[meilleur_conteneur] = [espace_initial]
            meilleur_espace = espace_initial

        # 3. Placer la marchandise en bas à gauche de l'espace choisi
        marchandise.x = meilleur_espace.x
        marchandise.y = meilleur_espace.y
        meilleur_conteneur.contenu.append(marchandise)

        # 4. Mettre à jour les espaces libres du conteneur choisi
        nouveaux_espaces_libres = []

        # Diviser TOUS les espaces libres qui sont touchés par cette nouvelle marchandise
        for espace in espaces_libres_par_conteneur[meilleur_conteneur]:
            nouveaux_espaces_libres.extend(diviser_espace(espace, marchandise))

        # 5. Nettoyage : Supprimer les espaces redondants (Pruning)
        # Un espace est supprimé s'il est entièrement contenu dans un autre
        espaces_epures = []
        for i, espace1 in enumerate(nouveaux_espaces_libres):
            est_redondant = False
            for j, espace2 in enumerate(nouveaux_espaces_libres):
                if i != j and espace2.contient(espace1):
                    est_redondant = True
                    break
            if not est_redondant:
                espaces_epures.append(espace1)

        espaces_libres_par_conteneur[meilleur_conteneur] = espaces_epures

    return train