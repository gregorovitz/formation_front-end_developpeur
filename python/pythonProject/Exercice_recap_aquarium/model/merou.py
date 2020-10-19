import random

from Interfaces.ipoissoncarnivore import IPoissonCarnivore
from model.poisson import Poisson


class Merou(Poisson, IPoissonCarnivore):
    def __init__(self, name, sexe):
        super().__init__(name, sexe)
    def manger(self,poisson):
        if not isinstance(poisson,Merou):
            retour=poisson.est_manger()
            self.gain_vie(5)
            if retour:
                return f'le {poisson.nom} a eté mangé par {self.nom}'
            else:
                return f'le {poisson.nom} est mort d\'avoir eté mangé par {self.nom}'


        else:
            self.faim()
            return f'le {poisson.nom} n\'a pas eté mangé par {self.nom} car il sont de la même espèce'
    def sereproduire(self, poison):
        if isinstance(poison,Merou) and self.sexe !=poison.sexe:
            merou=Merou(poison.nom+' '+self.nom,'m')
            return merou

    def veillir(self):
        super().veillir()
        if self.age == 10:
            self.sexe = 'f'