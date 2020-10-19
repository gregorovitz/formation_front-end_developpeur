from abc import ABC,abstractmethod


class IEtrevivant(ABC):

    @abstractmethod
    def perd_vie(self,value):
        pass
    @abstractmethod
    def gain_vie(self,value):
        pass
    @abstractmethod
    def veillir (self):
        pass

