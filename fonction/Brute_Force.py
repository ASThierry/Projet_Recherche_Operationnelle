from module.Objets import Objets,Objet
from fonction.decorator import *


@chronometrer
def brute_force(liste_objets, capacite_restante):
    return brute_force_recursif(liste_objets, capacite_restante)


def brute_force_recursif(liste_objets, capacite_restante, index=0):
    # Condition d'arrêt : on a parcouru tous les objets ou le sac est plein
    if index == len(liste_objets) or capacite_restante <= 0:
        return 0, []

    objet_actuel = liste_objets[index]

    # Branche A : On NE PREND PAS l'objet actuel
    utilite_sans, combinaison_sans = brute_force_recursif(
        liste_objets, capacite_restante, index + 1
    )

    # Branche B : On PREND l'objet actuel (uniquement si le poids le permet)
    utilite_avec = 0
    combinaison_avec = []

    if objet_actuel.masse <= capacite_restante:

        utilite_sous_arbre, combinaison_sous_arbre = brute_force_recursif(
            liste_objets, capacite_restante - objet_actuel.masse, index + 1
        )

        utilite_avec = objet_actuel.utilite + utilite_sous_arbre
        combinaison_avec = [objet_actuel] + combinaison_sous_arbre

    # 4. Comparaison : On retourne la meilleure des deux branches
    if utilite_avec > utilite_sans:
        return utilite_avec, combinaison_avec
    else:
        return utilite_sans, combinaison_sans