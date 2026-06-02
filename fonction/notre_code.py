from module.Objets import Objets
from module.Sac_a_dos import Sac

def notrefonction(liste_objets, capacite_sac):
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
        if obj.masse <= masse_restante:
            # ajoute de l'élément dans le  sac
            mon_sac.ajouter_element(obj)
            
            # On retire la masse de l'élément à la masse restante du sac
            masse_restante -= obj.masse
            
    # Renvoie le sac rempli
    return mon_sac

    from module.Objets import Objets
from module.Sac_a_dos import Sac
import copy

def backtracking_sac(liste_objets, capacite_max):
    # Variables pour stocker la meilleure solution trouvée pendant l'exploration
    meilleure_utilite = -1
    meilleur_sac = None

    def explorer(index, sac_actuel, masse_restante, utilite_actuelle):
        nonlocal meilleure_utilite, meilleur_sac

        # CONDITION D'ARRÊT / MISE À JOUR DE LA MEILLEURE SOLUTION
        # Si on a examiné tous les objets, on regarde si on a fait mieux qu'avant
        if index == len(liste_objets):
            if utilite_actuelle > meilleure_utilite:
                meilleure_utilite = utilite_actuelle
                # On fait une copie profonde du sac pour ne pas qu'il soit modifié par la suite
                meilleur_sac = copy.deepcopy(sac_actuel)
            return

        obj_actuel = liste_objets[index]

        # --- BRANCHEMENT 1 : L'ÉLÉMENT PEUT-IL ÊTRE AJOUTÉ ? (Pi est étendu) ---
        if obj_actuel.masse <= masse_restante:
            # ajout de l'objet dans le sac
            sac_actuel.ajouter_element(obj_actuel)
            
            # Récursion : On passe à l'objet suivant avec le sac mis à jour
            explorer(index + 1, sac_actuel, masse_restante - obj_actuel.masse, utilite_actuelle + obj_actuel.utilite)
            
            # Backtrack : On retire l'objet pour tester l'autre branche (sans cet objet)
            sac_actuel.retirer_element(obj_actuel) # <-- Supposant que cette méthode existe dans ta classe

        # ON N'AJOUTE PAS L'ÉLÉMENT 
        # On passe à l'objet suivant sans modifier le sac ni la masse
        explorer(index + 1, sac_actuel, masse_restante, utilite_actuelle)

    # Initialisation du problème racine P0
    sac_initial = Sac(capacite_max)
    
    # Lancement de la recherche à partir du premier objet (index 0)
    explorer(0, sac_initial, capacite_max, 0)

    # Si meilleure_utilite est restée à -1, c'est qu'aucune combinaison n'était possible
    if meilleur_sac is None:
        print("Il n'y a pas de solution")
        return None

    return meilleur_sac

