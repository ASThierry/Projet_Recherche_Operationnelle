from module.conteneur import Conteneur


class Train:
    def __init__(self):
        self.conteneurs : [Conteneur]= []
        


    def __str__(self):
        retour : str ="<====== Contenue du train ======>\n"
        i : int = 0
        for conteneur in self.conteneurs:
            retour += f"Le conteneur {i} contient :\n"
            retour += conteneur.__str__() + "\n"
            i+=1
        return retour

    def ajouter(self,conteneur: Conteneur):
        self.conteneur.append(conteneur)