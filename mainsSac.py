from module.Objets import Objets
from fonction.Glouton import Glouton_optimise
from fonction.Brute_Force import brute_force
from fonction.heuristique import heuristique

#==> Thierry
def testheuristique():
    objets = Objets()
    print("FONCTION HEURISTIQUE : ")
    sac = heuristique(objets.all,60)
    print(sac)
    print("\n")

#==>Thierry
def testGlouton_optimise():
     print("====== Glouton optimisé ======")
     objet = Objets()
     sac = Glouton_optimise(objet.all, 60)
     print(sac)
     print("\n")

#==> Mathis
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
    print("\n")

# ==> Mathis
def calculetemps():
    objets = Objets()
    capacite_sac = 60
    sac =None
    utilite_max = 0

    print("====== Calcule temps ======")
    for i in range(200):
        utilite_max, meilleure_selection = brute_force(objets.all, capacite_sac)
    print("====== Brute force ======")
    print(f"Utilité totale : {round(utilite_max, 3)}")

    print("====== Glouton optimisé ======")
    for i in range(200):
        sac = Glouton_optimise(objets.all, 60)
    print(f"Utilite Glouton : {sac.utilite_total()}")

    print("===== Heuristique =====")
    for i in range(200):
        sac = heuristique(objets.all, 60)
    print(f"Utilite Heuristique : {sac.utilite_total()}")

if __name__ == "__main__":
    #testbrute_force()
    #testGlouton_optimise()
    #testheuristique()
    calculetemps()