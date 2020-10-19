from abc import ABC, abstractmethod
from Interfaces.ipoisson import IPoisson
from model.algue import Algue


class IPoissonHerbivore( IPoisson):
    @abstractmethod
    def manger(self, poisson: Algue):
        pass