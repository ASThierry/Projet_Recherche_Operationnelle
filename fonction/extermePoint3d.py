from fonction.decorator import *
from module.marchandise import Marchandise
from module.conteneur import Conteneur
from module.train import Train
from fonction.Guillotine3d import obtenir_rotations

# Structure pour traquer les points d'ancrage en 3D
class ExtremePoint:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


def get_orientations(l, w, h):
        return list({(l, w, h), (l, h, w), (w, l, h), (w, h, l), (h, l, w), (h, w, l)})

def extremePoints3d_FirstFit(marchandises_triees : [Marchandise]):
    train = Train()
    # Dictionnaire pour lier un conteneur à sa liste de points extrêmes disponibles
    liste_extreme_points = {}
    for marchandise in marchandises_triees:
        place = False
        # Récupérer toutes les rotations possibles pour cette marchandise
        if marchandise.retournable == 1:
            orientations = get_orientations(marchandise.longueur, marchandise.largeur, marchandise.hauteur)
        else:
            orientations = [(marchandise.longueur, marchandise.largeur, marchandise.hauteur),( marchandise.largeur,marchandise.longueur, marchandise.hauteur)]

        # Chercher dans les conteneurs existants
        for conteneur in train.conteneurs:

            # OPTIMISATION : On trie la liste des points une seule fois avant de tester les points pour cette marchandise
            liste_extreme_points[conteneur].sort(key=lambda p: (p.z, p.y, p.x))

            # Chercher le premier point extrême et la première orientation qui valide le placement
            for i, pt in enumerate(liste_extreme_points[conteneur]):
                for dim_x, dim_y, dim_z in orientations:
                    # Vérifier si la marchandise ainsi orientée ne dépasse pas du conteneur
                    if (pt.x + dim_x <= conteneur.longueur and
                            pt.y + dim_y <= conteneur.largeur and
                            pt.z + dim_z <= conteneur.hauteur):

                        # Vérifier s'il n'y a pas de collision avec les objets déjà dedans
                        collision = False
                        for autre in conteneur.contenu:
                            # CRUCIAL : On compare avec les dimensions orientées (d_x, d_y, d_z) de l'autre objet
                            if not (pt.x + dim_x <= autre.x or pt.x >= autre.x + autre.longueur or
                                    pt.y + dim_y <= autre.y or pt.y >= autre.y + autre.largeur or
                                    pt.z + dim_z <= autre.z or pt.z >= autre.z + autre.hauteur):
                                collision = True
                                break

                        # Si le point et l'orientation sont valides, on pose !
                        if not collision:
                            marchandise.x = pt.x
                            marchandise.y = pt.y
                            marchandise.z = pt.z

                            # On sauvegarde les dimensions réelles occupées sur les axes
                            marchandise.longueur = dim_x
                            marchandise.largeur = dim_y
                            marchandise.hauteur = dim_z

                            conteneur.contenu.append(marchandise)

                            # Génération des 3 nouveaux points extrêmes (projections)
                            pt_x = ExtremePoint(pt.x + dim_x, pt.y, pt.z)
                            pt_y = ExtremePoint(pt.x, pt.y + dim_y, pt.z)
                            pt_z = ExtremePoint(pt.x, pt.y, pt.z + dim_z)

                            # Remplacer l'ancien point par les 3 nouveaux
                            liste_extreme_points[conteneur].pop(i)
                            liste_extreme_points[conteneur].extend([pt_x, pt_y, pt_z])

                            place = True
                            break  # Quitter la boucle des orientations
                if place:
                    break  # Quitter la boucle des points
            if place:
                break  # Passer à la marchandise suivante

        # Si aucun espace trouvé dans les conteneurs existants, on en ouvre un nouveau
        if not place:
            nouveau_conteneur = Conteneur()
            train.conteneurs.append(nouveau_conteneur)

            # On prend la première orientation par défaut pour le coin (0,0,0)
            orientation_valide = None
            for dim_x, dim_y, dim_z in orientations:
                if (dim_x <= nouveau_conteneur.longueur and
                        dim_y <= nouveau_conteneur.largeur and
                        dim_z <= nouveau_conteneur.hauteur):
                    orientation_valide = (dim_x, dim_y, dim_z)
                    break  # On s'arrête dès qu'on en trouve une qui rentre

            # Sécurité extrême (si la marchandise est physiquement trop grosse pour le train)
            if orientation_valide is None:
                print(f"ALERTE : La marchandise {marchandise.numero} est trop grande pour un conteneur !")
                dim_x, dim_y, dim_z = orientations[0]  # On la place quand même pour ne pas crasher
            else:
                dim_x, dim_y, dim_z = orientation_valide

            marchandise.x = 0
            marchandise.y = 0
            marchandise.z = 0
            marchandise.longueur = dim_x
            marchandise.largeur = dim_y
            marchandise.hauteur = dim_z

            nouveau_conteneur.contenu.append(marchandise)

            # Génération des 3 premiers points extrêmes autour de cette première marchandise
            pt_x = ExtremePoint(dim_x, 0, 0)
            pt_y = ExtremePoint(0, dim_y, 0)
            pt_z = ExtremePoint(0, 0, dim_z)

            liste_extreme_points[nouveau_conteneur] = [pt_x, pt_y, pt_z]

    return train

@chronometrer
def extremePoints3dOffline(marchandises_obj):
    # Tri hors-ligne (Offline) : Du plus grand volume au plus petit
    marchandises_triees = sorted(
        marchandises_obj.all,
        key=lambda m: m.getVolume(),
        reverse=True
    )
    return extremePoints3d_FirstFit(marchandises_triees)


@chronometrer
def extremePoints3dOnline(marchandises_obj):
    # Tri hors-ligne (Offline) : Du plus grand volume au plus petit
    marchandises_triees = marchandises_obj.all
    return extremePoints3d_FirstFit(marchandises_triees)