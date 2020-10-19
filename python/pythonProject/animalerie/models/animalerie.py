from models.animal import Animal
from models.chat import Chat
from models.chien import Chien
from models.oiseau import Oiseau
from tools import proba_generator


class Animalerie:
    def __init__(self):
        self.__animals = []

    @property
    def animals(self):
        result = []
        for a in self.__animals:
            if not a.is_death:
                yield a
                # result.append(a)
        # return tuple(result)
    @property
    def nb_animal(self):
        count=0
        for animal in self.animals:
            count+=1
        return count

    def add_animal(self, value: Animal):
        if isinstance(value, Animal) and not value.is_death:
            self.__animals.append(value)
        else:
            raise ValueError("bon animal!")

    def add_animals(self, *animals):

        for animal in animals:
            self.add_animal(animal)

    def affiche_animal(self):
        donnee = ''

        for animal in self.animals:
            donnee = donnee + animal.se_decrire()+'\n'
        return donnee

    def nombre_animal(self):
        chien = 0
        chat = 0
        oiseau = 0
        for animal in self.animals:
            if isinstance(animal, Chat):
                chat += 1
            elif isinstance(animal, Chien):
                chien += 1
            elif isinstance(animal, Oiseau):
                oiseau += 1
        return f'il y a {chat} chat, {chien} chien et {oiseau} oiseau dans l\'animalerie'

    def nouvel_journee(self):
        for animal in self.animals:
            animal.mort()
        for animal in self.animals:
            if isinstance(animal,Chat) and not animal.is_cut_griffe and proba_generator.generate_bool:
                print(f'{animal.name} griffe un visiteur')