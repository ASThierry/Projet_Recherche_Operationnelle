

class Objet():
    def __init__(self,nom : str , masse : float, utilite : float):
        self.nom = nom
        self.utilite = utilite
        self.masse = masse
        self.ratio = utilite / masse

    def __str__(self):
        return self.nom + " avec une utilité de " + str(self.utilite) + " et un poids de " + str(self.masse) + "kg"
