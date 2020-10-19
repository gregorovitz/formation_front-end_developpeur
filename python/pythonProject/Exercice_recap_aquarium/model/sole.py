import random

from Interfaces.ipoissonherbivore import IPoissonHerbivore
from model.poisson import Poisson


class Sole(Poisson, IPoissonHerbivore):
    def __init__(self, name, sexe):
        super().__init__(name, sexe)
    def manger(self,algue):
        self.gain_vie(3)
        retour = algue.est_manger()

        if retour:
            return f'l\'algue a eté mangé par {self.nom}'
        else:
            return f'l\'algue est morte d\'avoir eté mangé par {self.nom}'
    def sereproduire(self, poison):
        if isinstance(poison,Sole) :
            if self.sexe ==poison.sexe:
                if self.sexe=='m':
                    self.sexe='f'
                else:
                    self.sexe='m'
            rep=['f','m']
            coef=[1,1]
            sexe=random.choices(rep,coef)
            sole=Sole(poison.nom+' '+self.nom,sexe[0])

            return sole