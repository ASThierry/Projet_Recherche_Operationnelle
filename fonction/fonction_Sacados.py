class Sac:
    def __init__(self, poids):
        self.poids = poids
        self.contenus = []
        self.poids_restant = poids

    def ajouter_element(self, element):
        if element is None:
            raise ValueError("Impossible d'ajouter None au sac.")

        if element.poids > self.poids_restant:
            raise ValueError("Le poids de l'élément dépasse la capacité restante.")

        self.contenus.append(element)
        self.poids_restant -= element.poids

        if self.poids_restant == 0:
            print("Le sac est plein.")