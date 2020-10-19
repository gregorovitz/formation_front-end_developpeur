from datetime import datetime
import random
from abc import ABC


class Animal(ABC):
    def __init__(self, name, poids, taille, sexe, birthdate: datetime, date_arrive, cri='jce crie', prob_death=0.0):
        self.__name = name
        self.__poids = poids
        self.__taille = taille
        self.__sexe = sexe
        self.__birthdate = birthdate
        self.__date_arrive = date_arrive
        self.__cri = cri
        self.__prob_death = prob_death
        self.__death = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def poids(self):
        return self.__poids

    @poids.setter
    def poids(self, value):
        self.__poids = value

    @property
    def taille(self):
        return self.__taille

    @taille.setter
    def taille(self, value):
        self.__taille = value

    @property
    def sexe(self):
        return self.__sexe

    @sexe.setter
    def sexe(self, value):
        self.__sexe = value

    @property
    def birthdate(self):
        return self.__birthdate

    @birthdate.setter
    def birthdate(self, value):
        self.__birthdate = value

    @property
    def date_arrive(self):
        return self.__date_arrive

    @property
    def is_death(self):
        return self.__death

    @date_arrive.setter
    def date_arrive(self, value):
        self.__date_arrive = value

    @property
    def cri(self):
        return self.__cri

    @property
    def prob_death(self):
        return self.__prob_death

    @property
    def age(self):
        today = datetime.now()
        _age = today.year - self.birthdate.year
        if today.month < self.birthdate.month \
                or (today.month == self.birthdate.month and today.day < self.birthdate.day):
            _age -= 1
        return _age

    def crier(self):
        return self.cri

    def mort(self):
        reponse = ["Death", "not Death"]

        coefs = [self.prob_death, 1-self.prob_death]
        rep = random.choices(reponse, coefs)
        if rep[0] == "Death":
            self.__death = True

    def se_decrire(self):
        return f'nom : {self.name} poid :{self.poids} taille: {self.taille} age: {self.age} date d\'arrive :' \
               f'{self.date_arrive.strftime("%d %b %Y")}'