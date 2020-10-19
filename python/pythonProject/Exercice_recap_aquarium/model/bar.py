import random

from Interfaces.ipoissonherbivore import IPoissonHerbivore
from model.poisson import Poisson


class Bar(Poisson, IPoissonHerbivore):
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
        if isinstance(poison,Bar) and self.sexe !=poison.sexe:
            bar=Bar(poison.nom+' '+self.nom,'m')
            return bar
    def veillir(self):
        super().veillir()
        if self.age==10:
            self.sexe='f'