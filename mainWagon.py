from module.marchandises import Marchandises
from module.train import Train
from fonction.Offline2d import guillotine2dOffline, maxrects2dOffline
from fonction.Online2d import guillotine2dOnline
from fonction.Offline3d import guillotine3dOffline,guillotine3dOffline_split
from fonction.Offline2d import guillotine2dOffline
from fonction.extermePoint3d import *
from fonction.bestfit1d import bestfit1doffline,bestfit1doneline
from fonction.stockage1doffline import firstfit1doffline, firstfit1doneline

def test1d():
    marchandises = Marchandises()
    train  = Train()
    train1 = Train()
    train2 = Train()
    train3 = Train()
    firstfit1doffline(marchandises, train)
    firstfit1doneline(marchandises, train1)
    bestfit1doffline(marchandises, train2)
    bestfit1doneline(marchandises, train3)
    print(train3)


import random
import copy


def trouver_le_train_parfait(iterations=500):
    random.seed(123)
    marchandises_obj = Marchandises()
    # 1. On trie normalement pour avoir une bonne base
    base_liste = sorted(
        marchandises_obj.all,
        key=lambda m: (max(m.longueur, m.largeur, m.hauteur), m.getVolume()),
        reverse=True
    )

    meilleur_train = None
    min_conteneurs = float('inf')

    for i in range(iterations):
        # On copie la liste pour ne pas la détruire
        liste_test = copy.deepcopy(base_liste)

        # Sauf pour la première itération, on mélange un peu l'ordre (Mutation)
        if i > 0:
            # On prend 2 à 5 marchandises au hasard et on les échange de place
            nb_echanges = random.randint(1, 3)
            for _ in range(nb_echanges):
                idx1, idx2 = random.sample(range(len(liste_test)), 2)
                liste_test[idx1], liste_test[idx2] = liste_test[idx2], liste_test[idx1]

        # On crée un faux objet 'marchandises_obj' pour le passer à ton algo
        class FakeObj:
            pass

        fake = FakeObj()
        fake.all = liste_test

        # On lance TON algorithme (Guillotine ou Extreme Point)
        train_test = extremePoints3dOnline(fake)
        nb_conteneurs = len(train_test.conteneurs)

        # Si on bat le record, on sauvegarde !
        if nb_conteneurs < min_conteneurs:
            min_conteneurs = nb_conteneurs
            meilleur_train = train_test
            print(f"Nouvel optimum trouvé à l'itération {i} : {min_conteneurs} conteneurs !")

            # Si tu sais que 15 est le record absolu, tu peux t'arrêter plus tôt
            if min_conteneurs <= 15:
                print("Objectif atteint !")
                break

    return meilleur_train

def testOffline2d():
    marchandises = Marchandises()
    train: Train = guillotine2dOffline(marchandises)
    #train = maxrects2dOffline(marchandises)
    print(train)

def testOnline2d():
    marchandises = Marchandises()
    train: Train = guillotine2dOnline(marchandises)
    #print(train)

def testOffline3d():
    marchandises = Marchandises()
    #train: Train = guillotine3dOffline(marchandises)
    train : Train = guillotine3dOffline_split(marchandises)
    #print(train)
    train.affichage_reduit()
    train.afficher_graphique_3d()


def testextremePointOffline3d():
    marchandises = Marchandises()
    train = extremePoints3dOffline(marchandises)
    #print(train)
    train.affichage_reduit()
    train.afficher_graphique_3d()


def testExtremePointOnline3d():
    marchandises = Marchandises()
    train = extremePoints3dOnline(marchandises)
    #print(train)
    train.affichage_reduit()
    train.afficher_graphique_3d()


if __name__ == '__main__':
    #testOffline2d()
    #testextremePointOffline3d()
    #testExtremePointOnline3d()
    #testOffline2d()
    #testOnline2d()
    #testOffline3d()
    train = trouver_le_train_parfait()
    train.affichage_reduit()
    #train.afficher_graphique_3d()