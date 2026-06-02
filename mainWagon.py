from module.marchandises import Marchandises
from module.train import Train
from fonction.stockage1doffline import *
from fonction.bestfit1d import *

if __name__ == '__main__':
    marchandises = Marchandises()
    train  = Train()
    train1 = Train()
    train2 = Train()
    train3 = Train()
    firstfit1doffline(marchandises, train)
    firstfit1doneline(marchandises, train1)
    bestfit1doffline(marchandises, train2)
    bestfit1doneline(marchandises, train3)
    # print("Le nombre de conteneur total est : ",len(cont));
    print(train3)
    


