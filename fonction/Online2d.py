

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

@chronometrer
def guillotine2dOnline(marchandises_obj):
    train = Train()
    # Dictionnaire pour lier un conteneur à sa liste d'espaces libres
    espaces_libres = {}

    marchandises_triees = marchandises_obj.all

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