from abc import ABC, abstractmethod
from Interfaces.ipoisson import IPoisson


class IPoissonCarnivore(IPoisson):
    @abstractmethod
    def manger(self, poisson: IPoisson):
        pass