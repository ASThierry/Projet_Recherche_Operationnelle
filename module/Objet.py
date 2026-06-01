

class Objet():
    def __init__(self,nom : str , utilite : float, masse : float):
        self.nom = nom
        self.utilite = utilite
        self.masse = masse
        self.ratio = utilite / masse

    def __str__(self):
        print(self.nom + " avec une utilité de " + str(self.utilite) + " et un poids de " + str(self.masse) + "kg")
