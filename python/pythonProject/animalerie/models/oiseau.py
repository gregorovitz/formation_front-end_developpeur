from models.animal import Animal


class Oiseau(Animal):

    def __init__(self, name, poids, taille, sexe, birthdate, date_arrive, color, is_vollier=False):
        super().__init__(name, poids, taille, sexe, birthdate, date_arrive,"cui-cui",0.03)
        self.__color = color
        self.__is_vollier = is_vollier

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value
    @property
    def is_vollier(self):
        return self.__is_vollier

    @is_vollier.setter
    def is_vollier(self, value):
        self.__is_vollier = value

    def se_decrire(self):
        voilliere=''
        if self.is_vollier:
            voilliere='volière'
        else:
            voilliere='petite cage'

        return f'{super(Oiseau, self).se_decrire()} la couleur de l \'oiseau est: {self.color}  il vit dans une  {voilliere}'
