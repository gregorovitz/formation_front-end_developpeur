import random
from typing import List

from Interfaces.ipoissoncarnivore import IPoissonCarnivore
from Interfaces.ipoissonherbivore import IPoissonHerbivore
from model.poisson import Poisson


class Aquarium:
    def __init__(self,nom):
        self.__nom=nom
        self.__poissons=[]
        self.__algues=[]
    @property
    def poissons(self):
        result=[]
        for p in self.__poissons:
            if p.vivant:
                result.append(p)
        return tuple(result)

    @property
    def algues(self):
        result = []
        for a in self.__algues:
            if a.vivant:
                result.append(a)
        return tuple(result)

    def add_poisson(self,poisson):
        self.__poissons.append(poisson)
    
    def add_algue (self,algue):
        self.__algues.append(algue)

    def new_year(self):
        text=""
        mange = ''
        for poisson in self.poissons:

            if poisson.pv<=5 :
                if isinstance(poisson,IPoissonCarnivore):
                    eat_poisson=random.randint(0,len(self.poissons)-1)
                    mange=f"{mange} {poisson.manger(self.poissons[eat_poisson])}\n"

                if isinstance(poisson, IPoissonHerbivore):
                    if self.algues:
                        eat_algue = random.randint(0, len(self.algues)-1)
                        mange=f'{mange} {poisson.manger(self.algues[eat_algue])}\n'
            else:
                poisson.faim()
                rep_poisson = random.randint(0, len(self.poissons) - 1)
                baby=poisson.sereproduire(self.poissons[rep_poisson])
                if isinstance(baby,Poisson):
                    self.add_poisson(baby)
            text=f'{mange} \n'


        for poisson in self.poissons:
            is_trop_vieux=poisson.veillir()
            is_trop_vieux = poisson.age < 20

            if is_trop_vieux != True:
                text=f'{text} {poisson.nom} {is_trop_vieux}\n'
            else:
                text = f'{text} {poisson.nom} {poisson.sexe} pv:{poisson.pv} age:{poisson.age} \n'
        for algue in self.algues:
            if algue.pv>=10:
                self.add_algue(algue.sereproduire())

        for algue in self.algues:
            algue.veillir()
            is_trop_vieux = algue.age < 20
            if is_trop_vieux != True:
                text = f'{text} algue est mort de veillesse\n'
            else:
                text=f'{text} algues pv:{algue.pv} age: {algue.age}\n'
        return text