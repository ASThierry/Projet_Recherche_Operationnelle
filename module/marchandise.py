

class Marchandise:
    def __init__(self, numero,designation,longeur,largeur, hauteur):
        self.numero = numero
        self.designation = designation
        self.longeur = longeur
        self.largeur = largeur
        self.hauteur = hauteur


    def getlongeur(self):
        return self.longeur
    def getlargeur(self):
        return self.largeur
    def gethauteur(self):
        return self.hauteur

    def getSurface(self):
        return self.largeur*self.longeur

    def getVolume(self):
        return self.largeur*self.hauteur*self.hauteur


    def __str__(self):
        return f" -- {self.numero}. {self.designation} l : {self.longeur}, L: {self.largeur}m, h: {self.hauteur}m"