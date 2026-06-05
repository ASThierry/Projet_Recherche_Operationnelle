from module.marchandises import Marchandises
from module.train import Train
from module.conteneur import Conteneur
from fonction.decorator import *

# ==> Thierry
@chronometrer
def bestfit1doffline(marchandises, train): 
    #  Trier les marchandises par taille décroissante
    marchandises_trie = sorted(marchandises.all, key=lambda x: x.longueur, reverse=True)
    
    # Parcourir chaque marchandise triée
    for i in marchandises_trie:
        
        meilleur_wagon_index = None
        espace_restant_minimal = float('inf') # On commence avec une valeur infinie
        
        # Parcourir TOUS les wagons existants pour trouver le "Best Fit"
        for j in range(len(train.conteneurs)):
            espace_restant_apres = train.conteneurs[j].rest - i.longueur
            
            # Si la marchandise entre dans le wagon
            if espace_restant_apres >= 0:
                # Si cet espace restant est plus petit (plus optimisé) que ce qu'on a trouvé avant
                if espace_restant_apres < espace_restant_minimal:
                    espace_restant_minimal = espace_restant_apres
                    meilleur_wagon_index = j
                    
                # Si l'espace restant est exactement 0, on a trouvé le wagon idéal !
                if espace_restant_apres == 0:
                    break # Pas besoin de chercher plus loin pour cette marchandise
        
        # Une fois la boucle finie, on agit selon le résultat
        if meilleur_wagon_index is not None:
            # On place la marchandise dans le MEILLEUR wagon trouvé
            idx = meilleur_wagon_index
            train.conteneurs[idx].addmarchandise(i)          
            train.conteneurs[idx].rest -= i.longueur  
        else:
            # Si aucun wagon existant n'avait la place, on en crée un nouveau
            nouveau_wagon = Conteneur()
            nouveau_wagon.longueur = 11.583
            nouveau_wagon.rest = 11.583 
            
            nouveau_wagon.addmarchandise(i)         
            nouveau_wagon.rest -= i.longueur  
            train.conteneurs.append(nouveau_wagon)


# ==> Thierry
@chronometrer
def bestfit1doneline(marchandises, train): 
    # Parcourir chaque marchandise triée
    for i in marchandises.all:
        
        meilleur_wagon_index = None
        espace_restant_minimal = float('inf') # On commence avec une valeur infinie
        
        # 2. Parcourir TOUS les wagons existants pour trouver le "Best Fit"
        for j in range(len(train.conteneurs)):
            espace_restant_apres = train.conteneurs[j].rest - i.longueur
            
            # Si la marchandise entre dans le wagon
            if espace_restant_apres >= 0:
                # Si cet espace restant est plus petit (plus optimisé) que ce qu'on a trouvé avant
                if espace_restant_apres < espace_restant_minimal:
                    espace_restant_minimal = espace_restant_apres
                    meilleur_wagon_index = j
                    
                # CAS PARFAIT : Si l'espace restant est exactement 0, on a trouvé le wagon idéal !
                if espace_restant_apres == 0:
                    break # Pas besoin de chercher plus loin pour cette marchandise
        
        #  on agit selon le résultat
        if meilleur_wagon_index is not None:
            # On place la marchandise dans le MEILLEUR wagon trouvé
            idx = meilleur_wagon_index
            train.conteneurs[idx].addmarchandise(i)          
            train.conteneurs[idx].rest -= i.longueur  
        else:
            # Si aucun wagon existant n'avait la place, on en crée un nouveau
            nouveau_wagon = Conteneur()
            nouveau_wagon.longueur = 11.583
            nouveau_wagon.rest = 11.583 
            
            nouveau_wagon.addmarchandise(i)         
            nouveau_wagon.rest -= i.longueur  
            train.conteneurs.append(nouveau_wagon)