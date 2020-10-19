from model.etrevivant import Etrevivant


class Algue(Etrevivant):


    def __init__(self,pv=10):
        super().__init__(pv)

    def est_manger(self):
        retour=self.perd_vie(2)
        return retour
    def grandit(self):
        self.gain_vie(1)
    def veillir(self):
      self.grandit()
      super().veillir()

    def sereproduire(self):
        algue=Algue(5)
        self.perd_vie(5)
        return algue