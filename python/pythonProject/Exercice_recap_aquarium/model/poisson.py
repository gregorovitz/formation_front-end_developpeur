from Interfaces.ipoisson import IPoisson
from model.etrevivant import Etrevivant


class Poisson(Etrevivant,IPoisson):
    def __init__(self, nom, sexe):
        super(Poisson, self).__init__()
        self.__nom=nom
        self.__sexe=sexe

    @property
    def nom(self):
        return self.__nom
    
    @nom.setter
    def nom(self, value):
        self.__nom = value
    
    @property
    def sexe(self):
        return self.__sexe
    
    @sexe.setter
    def sexe(self, value):
        self.__sexe = value

    def manger(self, meal):
        pass

    def est_manger(self):
        is_eat=self.perd_vie(4)
        return is_eat

    def faim(self):
        is_death=self.perd_vie(1)
        return is_death

    def sereproduire(self, poison):
        pass

