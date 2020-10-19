from Interfaces.ietrevivant import IEtrevivant


class Etrevivant(IEtrevivant):
    def __init__(self,pv=10):
        self.__pv=pv
        self.__age=0
        self.__vivant=True

    @property
    def vivant(self):
        return self.__vivant
    @property
    def pv(self):
        return self.__pv
    @property
    def age(self):
        return self.__age

    def veillir(self):
        self.__age+=1
        if self.age==20:
            self.__vivant=False

    def perd_vie(self,value):
        self.__pv-=value
        if self.pv<=0:
            self.__vivant=False
            return False
        else:
            return True

    def gain_vie(self,value):
        self.__pv+=value

