from module.marchandise import Marchandise
# ===> Mathis
class Conteneur:

    def __init__(self):
        self.longueur = 11.583
        self.largeur = 2.294
        self.hauteur = 2.569
        self.rest =11.583
        self.contenu : [Marchandise]= []

    def __str__(self):
        retour : str= ""
        for contenu in self.contenu:
            retour += contenu.__str__() + "\n"
        return retour
    
    def addmarchandise(self, marchandise: Marchandise):
        self.contenu.append(marchandise)

    def getVolume(self):
        return self.longueur * self.largeur * self.hauteur

    def getVolumeOccupe(self):
        volume = 0
        for contenu in self.contenu:
            volume += contenu.getVolume()
        return volume

    def getVolumeRestante(self):
        return self.getVolume() - self.getVolumeOccupe()

    def affichage(self):
        print(f"Contient {len(self.contenu)} marchandises")
        print(f"Volume restant : {self.getVolumeRestante()}")



