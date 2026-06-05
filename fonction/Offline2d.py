"""
Fichier fait par Mathis
"""
from fonction.decorator import *
from module.conteneur import Conteneur
from module.train import Train

# Structure pour traquer les espaces vides
class EspaceLibre:
    def __init__(self, x, y, longueur, largeur):
        self.longueur = longueur
        self.x = x
        self.y = y
        self.largeur = largeur

    def contient(self, autre_espace):
        """Vérifie si cet espace englobe totalement un autre espace."""
        return (self.x <= autre_espace.x and
                self.y <= autre_espace.y and
                self.x + self.longueur >= autre_espace.x + autre_espace.longueur and
                self.y + self.largeur >= autre_espace.y + autre_espace.largeur)


def guillotine2d(marchandises_triees):
    train = Train()
    # Dictionnaire pour lier un conteneur à sa liste d'espaces libres
    espaces_libres = {}
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

@chronometrer
def guillotine2dOffline(marchandises_obj):
    # Tri hors-ligne (Offline) : Du plus grand au plus petit (très important pour Guillotine)
    # On utilise ta méthode getSurface()
    marchandises_triees = sorted(marchandises_obj.all, key=lambda m: m.largeur, reverse=True)
    return guillotine2d(marchandises_triees)

