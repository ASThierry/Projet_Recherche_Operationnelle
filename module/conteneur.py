from module.marchandise import Marchandise

class Conteneur:

    def __init__(self):
        self.longueur = 11.583
        self.largeur = 2.294
        self.hauteur = 2.569
        self.contenu : [Marchandise]= []

    def __str__(self):
        retour : str= ""
        for contenu in self.contenu:
            retour += contenu.__str__() + "\n"
        return retour




