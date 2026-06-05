
from fonction.decorator import *
from module.marchandises import Marchandises

from fonction.Offline2d import guillotine2d

# Structure pour traquer les espaces vides
class EspaceLibre:
    def __init__(self, x, y, longueur, largeur):
        self.x = x
        self.y = y
        self.longueur = longueur
        self.largeur = largeur

#==> Mathis Letellier
@chronometrer
def guillotine2dOnline(marchandises_obj : Marchandises):
    marchandises_triees = marchandises_obj.all
    return guillotine2d(marchandises_triees)