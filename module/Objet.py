
# ==> Mathis et Thierry
class Objet:
    def __init__(self,nom : str , masse : float, utilite : float):
        self.nom = nom
        self.utilite = utilite
        #passage du poids en gramme pour les arrondies fais par la machine sur la virgule
        self.masse : int = int(masse*100)
        self.ratio = utilite / masse
        self.pris = 0

    def prendre(self):
        self.pris = 1

    def enlever(self):
        self.pris = 0

    def __str__(self):
        return f" - {self.nom} ({self.masse} g, utilité: {self.utilite})"
