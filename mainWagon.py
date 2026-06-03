from module.marchandises import Marchandises
from module.train import Train
from fonction.Offline2d import guillotine2dOffline, maxrects2dOffline
from fonction.Online2d import guillotine2dOnline
from fonction.Offline3d import guillotine3dOffline,guillotine3dOffline_split

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
    print(train)



if __name__ == '__main__':
    #testOffline2d()
    #testOnline2d()
    testOffline3d()