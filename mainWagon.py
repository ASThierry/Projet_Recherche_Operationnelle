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


def testextremePoint3d():
    marchandises = Marchandises()
    train = extremePoints3dOffline(marchandises)
    #print(train)
    train.affichage_reduit()


if __name__ == '__main__':
    #testOffline2d()
    testextremePoint3d()
    #testOffline2d()
    #testOnline2d()
    #testOffline3d()