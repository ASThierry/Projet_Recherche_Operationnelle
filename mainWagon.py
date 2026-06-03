from module.marchandises import Marchandises
from module.train import Train
from fonction.Offline2d import guillotine2dOffline
from fonction.extermePoint3d import *

def testOffline2d():
    marchandises = Marchandises()
    train: Train = guillotine2dOffline(marchandises)


def testextermePoint3doneline():
    marchandises = Marchandises()
    train = extremePoints3dOneline(marchandises)
    print(train)


def testextermePoint3d():
    marchandises = Marchandises()
    train = extremePoints3dOffline(marchandises)
    print(train)
    

if __name__ == '__main__':
    #testOffline2d()
    testextermePoint3d()
    testextermePoint3doneline()