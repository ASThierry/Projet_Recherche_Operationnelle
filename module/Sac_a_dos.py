#==> Thierry
class Sac:
    def __init__(self, poids):
        self.poids = poids
        self.contenus = []
        self.poids_restant = poids


    def ajouter_element(self, element):
        if element is None:
            raise ValueError("Impossible d'ajouter None au sac.")

        if element.masse > self.poids_restant:
            raise ValueError("Le poids de l'élément dépasse la capacité restante.")

        self.contenus.append(element)
        self.poids_restant -= element.masse

        if self.poids_restant == 0:
            #print("Le sac est plein.")
            pass

    
    def __str__(self):
        retour = "<======= Contenue du sac =======>\n"
        retour += f"Utilité totale : {round(self.utilite_total(),3)}\n"
        for i in self.contenus:
            retour += i.__str__() + "\n"
        return retour


    def utilite_total(self):
        total = 0
        for i in self.contenus:
            total += i.utilite
        return total