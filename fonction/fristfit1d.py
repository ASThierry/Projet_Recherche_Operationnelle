from fonction.decorator import chronometrer
from module.marchandises import Marchandises
from module.train import Train
from module.conteneur import Conteneur
"""
    Idée de l'algorithme First-Fit Offline (1D) :
    1. Trier les marchandises par taille décroissante.
    2. Pour chaque marchandise, parcourir les wagons (conteneurs) existants.
    3. Placer la marchandise dans le premier wagon qui a assez d'espace disponible.
    4. Si aucun wagon existant ne convient, on crée un nouveau wagon.
"""
@chronometrer
def firstfit1doffline(marchandises, train): 
    # Trier les marchandises
    marchandises_trie = sorted(marchandises.all, key=lambda x: x.longueur, reverse=True)
    # Parcourir chaque marchandise triée
    for i in marchandises_trie:
        # Indicateur pour savoir si la marchandise a trouvé un wagon
        placee = False
        
        # Parcourir les wagons déjà existants dans le train
        for j in range(len(train.conteneurs)):
            # Vérifier si l'espace restant dans le wagon j est suffisant
            # train[j].longueur représente l'espace restant
            if i.longueur <= train.conteneurs[j].rest:
                train.conteneurs[j].addmarchandise(i)          
                train.conteneurs[j].rest -= i.longueur  
                placee = True            
                break                      
        
        #  Si aucun wagon existant n'avait la place, on crée un nouveau wagon
        if not placee:
            nouveau_wagon = Conteneur()
            nouveau_wagon.longueur = 11.583
            nouveau_wagon.addmarchandise(i)         
            nouveau_wagon.rest -= i.longueur  
            train.conteneurs.append(nouveau_wagon)      
            
    
@chronometrer
def firstfit1doneline(marchandises, train): 
    # Parcourir chaque marchandise triée
    for i in marchandises.all:
      # Indicateur pour savoir si la marchandise a trouvé un wagon
        placee = False
        
        # Parcourir les wagons déjà existants dans le train
        for j in range(len(train.conteneurs)):
            # Vérifier si l'espace restant dans le wagon j est suffisant
            # train[j].longueur représente l'espace restant
            if i.longueur <= train.conteneurs[j].rest:
                train.conteneurs[j].addmarchandise(i)          
                train.conteneurs[j].rest -= i.longueur  
                placee = True            
                break                      
        
        #  Si aucun wagon existant n'avait la place, on crée un nouveau wagon
        if not placee:
            nouveau_wagon = Conteneur()
            nouveau_wagon.longueur = 11.583
            nouveau_wagon.addmarchandise(i)         
            nouveau_wagon.rest -= i.longueur  
            train.conteneurs.append(nouveau_wagon)      
            
    