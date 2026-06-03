from module.conteneur import Conteneur


class Train:
    def __init__(self):
        self.conteneurs : [Conteneur]= []
        


    def __str__(self):
        retour : str ="<====== Contenue du train ======>\n"
        i : int = 1
        for conteneur in self.conteneurs:
            retour += f"Le conteneur {i} contient :\n"
            retour += conteneur.__str__() + "\n"
            i+=1
        return retour

    def ajouter(self,conteneur: Conteneur):
        self.conteneurs.append(conteneur)

    def affichage_reduit(self):
        print("<===== Le train ( affichage reduit )======>")
        print(f"Le nombre de wagon est {len(self.conteneurs)}")
        volume : int = 0
        for i in range(len(self.conteneurs)):
            print(f"--- Wagon n° {i+1}")
            volume += self.conteneurs[i].getVolumeRestante()
            self.conteneurs[i].affichage()
        print(f"<===== il reste dans le train : {volume} m² de libre =====>")


