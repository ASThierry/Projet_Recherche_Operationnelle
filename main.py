from module.Objets import Objets,Objet
from fonction.Brute_Force import brute_force
from fonction.heuristique import heuristique
from time import time

def heurist():
    objets = Objets()
    print("FONCTION HEURISTIQUE : ")
    sac = heuristique(objets.all,60)
    print(sac)
    print("FIN DE LA FONCTION HEURISTIQUE. ")

if __name__ == "__main__":

    sac = Objets()
    for i in sac.getall():
        print(i)

    capacite_sac = 0.6

    utilite_max, meilleure_selection = brute_force(sac.all, capacite_sac)

    # 4. Affichage du résultat
    print("\n=== RÉSULTAT OPTIMAL ===")
    print(f"Utilité totale : {round(utilite_max,3)}")
    print("Objets à emporter :")
    for obj in meilleure_selection:
        print(f" - {obj.nom} ({obj.masse} g, utilité: {obj.utilite})")

    heurist()



