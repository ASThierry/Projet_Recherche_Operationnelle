from module.marchandises import Marchandises
from module.train import Train
from fonction.Online2d import guillotine2dOnline
from fonction.Guillotine3d import guillotine3dOffline,guillotine3dOnline,guillotine3dOffline_opti,guillotine3dOnline_opti
from fonction.Offline2d import guillotine2dOffline
from fonction.extermePoint3d import extremePoints3dOnline,extremePoints3dOffline
from fonction.bestfit1d import bestfit1doffline,bestfit1doneline
from fonction.fristfit1d import firstfit1doffline, firstfit1doneline
from fonction.extermePoint3d_challenge_temp import extremePoints3dOnline_challenge, extremePoints3dOffline_challenge
import random
import copy

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


def testOffline2d():
    marchandises = Marchandises()
    train: Train = guillotine2dOffline(marchandises)
    #train = maxrects2dOffline(marchandises)
    #print(train)
    #train.affichage_reduit()
    train.affiche_mini()
    print("\n")

def testOnline2d():
    print("")
    marchandises = Marchandises()
    train: Train = guillotine2dOnline(marchandises)
    #print(train)
    train.affiche_mini()
    print("\n")

def testGuillotineOffline3d():
    marchandises = Marchandises()
    #train: Train = guillotine3dOffline(marchandises)
    train : Train = guillotine3dOffline_opti(marchandises)
    #print(train)
    #train.affichage_reduit()
    train.affiche_mini()
    #train.afficher_graphique_3d()
    print("\n")


def testGuillotineOnline3d():
    marchandises = Marchandises()
    # train: Train = guillotine3dOffline(marchandises)
    train: Train = guillotine3dOnline_opti(marchandises)
    # print(train)
    train.affichage_reduit()
    # train.afficher_graphique_3d()
    print("\n")

def testExtremePointOffline3d():
    marchandises = Marchandises()
    train = extremePoints3dOffline(marchandises)
    #print(train)
    train.affichage_reduit()
    train.afficher_graphique_3d()
    print("\n")


def testExtremePointOnline3d():
    marchandises = Marchandises()
    train = extremePoints3dOnline(marchandises)
    #print(train)
    train.affichage_reduit()
    train.afficher_graphique_3d()
    print("\n")

def CalculeMoyenneTemps(iteration : int = 100):
    train: Train = None

    # analyse de temps du 1d Online avec guillotine
    print("<===== Debut de l'annalyse de 1d online First FIT ======>")
    for it in range(iteration):
        marchandises = Marchandises()
        train: Train = Train()
        firstfit1doneline(marchandises, train)
    train.affiche_mini()

    # analyse de temps du 2d Offline avec guillotine
    print("<===== Debut de l'annalyse de 1d offline avec first FIT ======>")
    for it in range(iteration):
        marchandises = Marchandises()
        train: Train = Train()
        firstfit1doffline(marchandises, train)
    train.affiche_mini()

    # analyse de temps du 1d Online avec guillotine
    print("<===== Debut de l'annalyse de 1d online BEST FIT ======>")
    for it in range(iteration):
        marchandises = Marchandises()
        train: Train = Train()
        bestfit1doneline(marchandises,train)
    train.affiche_mini()

    # analyse de temps du 2d Offline avec guillotine
    print("<===== Debut de l'annalyse de 1d offline avec BEST FIT ======>")
    for it in range(iteration):
        marchandises = Marchandises()
        train: Train = Train()
        bestfit1doffline(marchandises,train)
    train.affiche_mini()

    #analyse de temps du 2d Online avec guillotine
    print("<===== Debut de l'annalyse de 2d online avec guillotine ======>")
    for it in range(iteration):
        marchandises = Marchandises()
        train: Train = guillotine2dOnline(marchandises)
    train.affiche_mini()

    # analyse de temps du 2d Offline avec guillotine
    print("<===== Debut de l'annalyse de 2d offline avec guillotine ======>")
    for it in range(iteration):
        marchandises = Marchandises()
        train: Train = guillotine2dOffline(marchandises)
    train.affiche_mini()

    # analyse de temps du 3d Online avec guillotine
    print("<===== Debut de l'annalyse de 3d online avec guillotine ======>")
    for it in range(iteration):
        marchandises = Marchandises()
        train: Train = guillotine3dOnline(marchandises)
    train.affiche_mini()

    # analyse de temps du 3d Offline avec guillotine
    print("<===== Debut de l'annalyse de 3d offline avec guillotine ======>")
    for it in range(iteration):
        marchandises = Marchandises()
        train: Train = guillotine3dOffline(marchandises)
    train.affiche_mini()

    # analyse de temps du 3d Offline avec guillotine opti
    print("<===== Debut de l'annalyse de 3d offline avec guillotine opti ======>")
    for it in range(iteration):
        marchandises = Marchandises()
        train: Train = guillotine3dOffline_opti(marchandises)
    train.affiche_mini()

    # analyse de temps du 3d Online avec guillotine opti
    print("<===== Debut de l'annalyse de 3d online avec guillotine opti ======>")
    for it in range(iteration):
        marchandises = Marchandises()
        train: Train = guillotine3dOnline_opti(marchandises)
    train.affiche_mini()

    # analyse de temps du 3d Offline avec extrem poit
    print("<===== Debut de l'annalyse de 3d offline avec extrem point ======>")
    for it in range(iteration):
        marchandises = Marchandises()
        train: Train = extremePoints3dOnline(marchandises)
    train.affiche_mini()

    # analyse de temps du 3d Online avec extrem point
    print("<===== Debut de l'annalyse de 3d online avec extern point ======>")
    for it in range(iteration):
        marchandises = Marchandises()
        train: Train = extremePoints3dOffline(marchandises)
    train.affiche_mini()

def ChalengeTemps(iteration = 500):
    train :Train
    # analyse de temps du 3d Online avec extrem point
    print("<===== Debut de l'annalyse de 3d offline avec extern point challenge temps ======>")
    for it in range(iteration):
        marchandises = Marchandises()
        train: Train = extremePoints3dOffline_challenge(marchandises)
    train.affiche_mini()

    print("<===== Debut de l'annalyse de 3d online avec extern point challenge temps ======>")
    for it in range(iteration):
        marchandises = Marchandises()
        train: Train = extremePoints3dOnline_challenge(marchandises)
    train.affiche_mini()


def test_extremePoints3dOnline_chalenge():
    marchandises = Marchandises()
    train: Train = extremePoints3dOnline_challenge(marchandises)
    train.affiche_mini()
    train: Train = extremePoints3dOffline_challenge(marchandises)
    train.affiche_mini()


if __name__ == '__main__':
    #testOffline2d()
    #testExtremePointOnline3d()
    #testExtremePointOffline3d()
    #testOffline2d()
    #testOnline2d()
    #testGuillotineOffline3d()
    #testGuillotineOnline3d()
    #train = trouver_le_train_parfait()
    #train.affichage_reduit()
    #train.afficher_graphique_3d()
    #CalculeMoyenneTemps()
    #ChalengeTemps()
    test_extremePoints3dOnline_chalenge()

def trouver_le_train_parfait(iterations=5000):
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
        train_test = guillotine3dOffline_opti(fake)
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