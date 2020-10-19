from abc import ABC,abstractmethod


class IPoisson(ABC):

   @abstractmethod
   def manger(self, meal):
      pass
   @abstractmethod
   def faim(self):
      pass
   @abstractmethod
   def sereproduire(self,poison):
      pass