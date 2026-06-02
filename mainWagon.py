from module.marchandises import Marchandises
from module.train import Train
from fonction.stockage1doffline import *

if __name__ == '__main__':
    marchandises = Marchandises()
    train =Train()
    train1 = Train()
    firstfit1doffline(marchandises, train)
    firstfit1doneline(marchandises, train1)
    # print("Le nombre de conteneur total est : ",len(cont));
    print(train)
    print(train1)


