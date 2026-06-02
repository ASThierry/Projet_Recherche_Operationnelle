

class Marchandise:
    def __init__(self, numero,designation,longueur,largeur, hauteur):
        self.numero = numero
        self.designation = designation
        self.longueur = longueur
        self.largeur = largeur
        self.hauteur = hauteur


    def getlongeur(self):
        return self.longueur
    def getlargeur(self):
        return self.largeur
    def gethauteur(self):
        return self.hauteur

    def getSurface(self):
        return self.largeur*self.longueur

    def getVolume(self):
        return self.largeur*self.hauteur*self.longueur


    def __str__(self):
        return f" -- {self.numero}. {self.designation} l : {self.longueur}, L: {self.largeur}m, h: {self.hauteur}m"