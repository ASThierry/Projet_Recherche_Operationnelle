from fonction.decorator import *
from module.marchandise import Marchandise
from module.conteneur import Conteneur
from module.train import Train

# Structure pour traquer les points d'ancrage en 3D
class ExtremePoint:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

@chronometrer
def extremePoints3dOffline(marchandises_obj):
    # je cherche aussi a faire des rotation et optiniser le code pour mettre le plus de marchandire sans les wagon avec des rotatin
    train = Train()
    # Dictionnaire pour lier un conteneur à sa liste de points extrêmes disponibles
    liste_extreme_points = {}

    # Tri hors-ligne (Offline) : Du plus grand volume au plus petit 
    # (Idéal pour compacter en 3D : Longueur * Largeur * Hauteur)
    marchandises_triees = sorted(
        marchandises_obj.all, 
        key=lambda m: m.longueur * m.largeur * m.hauteur, 
        reverse=True
    )

    for marchandise in marchandises_triees:
        place = False

        # Chercher dans les conteneurs existants
        for conteneur in train.conteneurs:
            
            # Tri des points pour faire du Best-Fit (Priorité au sol Z, puis fond Y, puis X)
            liste_extreme_points[conteneur] = sorted(
                liste_extreme_points[conteneur], 
                key=lambda p: (p.z, p.y, p.x)
            )

            # Chercher le premier point extrême disponible (First Fit parmi les triés)
            for i, pt in enumerate(liste_extreme_points[conteneur]):
                
                #  Vérifier si la marchandise ne dépasse pas du conteneur
                if (pt.x + marchandise.longueur <= conteneur.longueur and
                    pt.y + marchandise.largeur <= conteneur.largeur and
                    pt.z + marchandise.hauteur <= conteneur.hauteur):
                    
                    # Vérifier s'il n'y a pas de collision avec les objets déjà dedans
                    collision = False
                    for autre in conteneur.contenu:
                        # Si ça se chevauche sur les 3 axes en même temps -> Collision
                        if not (pt.x + marchandise.longueur <= autre.x or pt.x >= autre.x + autre.longueur or
                                pt.y + marchandise.largeur <= autre.y or pt.y >= autre.y + autre.largeur or
                                pt.z + marchandise.hauteur <= autre.z or pt.z >= autre.z + autre.hauteur):
                            collision = True
                            break
                    
                    # Si le point est valide et sans collision, on pose !
                    if not collision:
                        # Assigner la position 3D finale à la marchandise
                        marchandise.x = pt.x
                        marchandise.y = pt.y
                        marchandise.z = pt.z

                        # Ajouter au conteneur
                        conteneur.contenu.append(marchandise)

                        # Génération des 3 nouveaux points extrêmes (projections)
                        pt_x = ExtremePoint(pt.x + marchandise.longueur, pt.y, pt.z)
                        pt_y = ExtremePoint(pt.x, pt.y + marchandise.largeur, pt.z)
                        pt_z = ExtremePoint(pt.x, pt.y, pt.z + marchandise.hauteur)

                        # Remplacer l'ancien point par les 3 nouveaux
                        liste_extreme_points[conteneur].pop(i)
                        liste_extreme_points[conteneur].extend([pt_x, pt_y, pt_z])

                        place = True
                        break

            if place:
                break # On passe à la marchandise suivante

        # Si aucun espace trouvé dans les conteneurs existants, on en ouvre un nouveau
        if not place:
            nouveau_conteneur = Conteneur()
            train.conteneurs.append(nouveau_conteneur)

            # On place l'objet à l'origine du nouveau conteneur (0, 0, 0)
            marchandise.x = 0
            marchandise.y = 0
            marchandise.z = 0
            nouveau_conteneur.contenu.append(marchandise)

            # Génération des 3 premiers points extrêmes autour de cette première marchandise
            pt_x = ExtremePoint(marchandise.longueur, 0, 0)
            pt_y = ExtremePoint(0, marchandise.largeur, 0)
            pt_z = ExtremePoint(0, 0, marchandise.hauteur)

            liste_extreme_points[nouveau_conteneur] = [pt_x, pt_y, pt_z]

    return train

@chronometrer
def extremePoints3dOneline(marchandises_obj):
    train = Train()
    # Dictionnaire pour lier un conteneur à sa liste de points extrêmes disponibles
    liste_extreme_points = {}

    # Tri hors-ligne (Offline) : Du plus grand volume au plus petit 
    # (Idéal pour compacter en 3D : Longueur * Largeur * Hauteur)
    marchandises_triees =marchandises_obj.all
       

    for marchandise in marchandises_triees:
        place = False

        # Chercher dans les conteneurs existants
        for conteneur in train.conteneurs:
            
            # Tri des points pour faire du Best-Fit (Priorité au sol Z, puis fond Y, puis X)
            liste_extreme_points[conteneur] = sorted(
                liste_extreme_points[conteneur], 
                key=lambda p: (p.z, p.y, p.x)
            )

            # Chercher le premier point extrême disponible (First Fit parmi les triés)
            for i, pt in enumerate(liste_extreme_points[conteneur]):
                
                #  Vérifier si la marchandise ne dépasse pas du conteneur
                if (pt.x + marchandise.longueur <= conteneur.longueur and
                    pt.y + marchandise.largeur <= conteneur.largeur and
                    pt.z + marchandise.hauteur <= conteneur.hauteur):
                    
                    # Vérifier s'il n'y a pas de collision avec les objets déjà dedans
                    collision = False
                    for autre in conteneur.contenu:
                        # Si ça se chevauche sur les 3 axes en même temps -> Collision
                        if not (pt.x + marchandise.longueur <= autre.x or pt.x >= autre.x + autre.longueur or
                                pt.y + marchandise.largeur <= autre.y or pt.y >= autre.y + autre.largeur or
                                pt.z + marchandise.hauteur <= autre.z or pt.z >= autre.z + autre.hauteur):
                            collision = True
                            break
                    
                    # Si le point est valide et sans collision, on pose !
                    if not collision:
                        # Assigner la position 3D finale à la marchandise
                        marchandise.x = pt.x
                        marchandise.y = pt.y
                        marchandise.z = pt.z
                        
                        # Ajouter au conteneur
                        conteneur.contenu.append(marchandise)

                        # Génération des 3 nouveaux points extrêmes (projections)
                        pt_x = ExtremePoint(pt.x + marchandise.longueur, pt.y, pt.z)
                        pt_y = ExtremePoint(pt.x, pt.y + marchandise.largeur, pt.z)
                        pt_z = ExtremePoint(pt.x, pt.y, pt.z + marchandise.hauteur)

                        # Remplacer l'ancien point par les 3 nouveaux
                        liste_extreme_points[conteneur].pop(i)
                        liste_extreme_points[conteneur].extend([pt_x, pt_y, pt_z])

                        place = True
                        break

            if place:
                break # marchandise suivante

        # Si aucun espace trouvé dans les conteneurs existants, on en ouvre un nouveau
        if not place:
            nouveau_conteneur = Conteneur()
            train.conteneurs.append(nouveau_conteneur)

            # On place l'objet à l'origine du nouveau conteneur (0, 0, 0)
            marchandise.x = 0
            marchandise.y = 0
            marchandise.z = 0
            nouveau_conteneur.contenu.append(marchandise)

            # Génération des 3 premiers points extrêmes autour de cette première marchandise
            pt_x = ExtremePoint(marchandise.longueur, 0, 0)
            pt_y = ExtremePoint(0, marchandise.largeur, 0)
            pt_z = ExtremePoint(0, 0, marchandise.hauteur)

            liste_extreme_points[nouveau_conteneur] = [pt_x, pt_y, pt_z]

    return train


# je cherche aussi a faire des rotation et optiniser le code pour mettre le plus de marchandire sans les wagon avec des rotatin