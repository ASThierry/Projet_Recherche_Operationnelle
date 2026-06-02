from module.Objets import Objets,Objet
from fonction.notre_code import Glouton_optimise
from fonction.Brute_Force import brute_force
from time import time



def testnotrefonction():
     print("====== Glouton optimisé ======")
     objet = Objets()
     sac = Glouton_optimise(objet.all, 60)

     print(sac)

def testbrute_force():
    sac = Objets()

    capacite_sac = 60

    utilite_max, meilleure_selection = brute_force(sac.all, capacite_sac)

    # Affichage du résultat
    print("====== Brute force ======")
    print(f"Utilité totale : {round(utilite_max, 3)}")
    print("Objets à emporter :")
    for obj in meilleure_selection:
        print(f" - {obj.nom} ({obj.masse} g, utilité: {obj.utilite})")

if __name__ == "__main__":
    testbrute_force()
    testnotrefonction()