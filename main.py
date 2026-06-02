from module.Objets import Objets
from fonction.notre_code import notrefonction

if __name__ == "__main__":
    objet = Objets()
    # sac = notrefonction(objet.all, 0.6)
    sac1 = notrefonction(objet, 0.6)
    print(sac1)
   

