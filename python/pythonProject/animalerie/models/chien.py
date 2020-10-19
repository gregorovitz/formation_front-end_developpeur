from models.animal import Animal


class Chien(Animal):

    def __init__(self, name, poids, taille, sexe, birthdate, date_arrive, color, race, is_dresse=False):
        super().__init__(name, poids, taille, sexe, birthdate, date_arrive, "wouf", 0.01)
        self.__color_colier = color
        self.__is_dresse = is_dresse
        self.__race = race

    @property
    def color_colier(self):
        return self.__color_colier
    
    @color_colier.setter
    def color_colier(self, value):
        self.__color_colier = value
    
    @property
    def is_dresse(self):
        return self.__is_dresse

    def follow_dresse(self):
        self.__is_dresse = True

    @property
    def race(self):
        return self.__race
    
    @race.setter
    def race(self, value):
        self.__race = value

    def se_decrire(self):

        if self.is_dresse:
            dresse = 'est dressé'
        else:
            dresse = "n'est pas dressé"
        return f'{super(Chien, self).se_decrire()} la couleur du collier est : {self.color_colier}' \
               f' la race du chien  un : {self.race} le chien  {dresse}'
