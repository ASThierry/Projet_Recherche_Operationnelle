from module.marchandises import Marchandises
from module.train import Train
from fonction.Offline2d import guillotine2dOffline

def testOffline2d():
    marchandises = Marchandises()
    train: Train = guillotine2dOffline(marchandises)
    #print(train)


if __name__ == '__main__':
    testOffline2d()