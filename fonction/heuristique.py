from module.Objets import Objets
from module.Sac_a_dos import Sac
from fonction.decorator import *
import copy

@chronometrer
def heuristique(liste_objets, capacite_sac):
    #initialiser le sac avec sa capacité maximale
    mon_sac = Sac(capacite_sac) 
    masse_restante = capacite_sac
    
    # trie les objets par rapport à leur ratio utilité/masse 
    objets_tries = sorted(liste_objets, key=lambda x: x.ratio, reverse=True)
    # Parcoutrir nos objet
    for obj in objets_tries:
        # Si le sac est déjà plein, on arrête tout immédiatement
        if masse_restante == 0:
            return mon_sac
            
        # vérifie si la masse de l'objet est inférieure ou égale à la masse restante
        if obj.masse <= masse_restante and obj.utilite > 1.0:
            # ajoute de l'élément dans le  sac
            mon_sac.ajouter_element(obj)
            
            # On retire la masse de l'élément à la masse restante du sac
            masse_restante -= obj.masse
            
    # Renvoie le sac rempli
    return mon_sac