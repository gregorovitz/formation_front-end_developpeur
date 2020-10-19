import random

from Interfaces.ipoissoncarnivore import IPoissonCarnivore
from model.poisson import Poisson


class Poissonclown(Poisson, IPoissonCarnivore):
    def __init__(self, name, sexe):
        super().__init__(name, sexe)

    def manger(self, poisson):
        if not isinstance(poisson,Poissonclown):
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
        if isinstance(poison,Poissonclown) and self.sexe !=poison.sexe:
            if self.sexe ==poison.sexe:
                if self.sexe=='m':
                    self.sexe='f'
                else:
                    self.sexe='m'
            rep=['f','m']
            coef=[1,1]
            sexe=random.choices(rep,coef)
            poisson=Poissonclown(poison.nom+' '+self.nom,sexe[0])
            return poisson

