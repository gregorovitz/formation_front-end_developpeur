from models.animal import Animal


class Chat(Animal):

    def __init__(self, name, poids, taille, sexe, birthdate, date_arrive, caracter, is_poil_long=False,
                 is_cut_griffe=False):
        super().__init__(name, poids, taille, sexe, birthdate, date_arrive, "Miawou", 0.05)
        self.__caracter = caracter
        self.__is_claw_cut = is_cut_griffe
        self.__is_poil_long = is_poil_long

    @property
    def caracter(self):
        return self.__caracter
    
    @caracter.setter
    def caracter(self, value):
        self.__caracter = value
    
    @property
    def is_cut_griffe(self):
        return self.__is_claw_cut
    
    @is_cut_griffe.setter
    def is_cut_griffe(self, value):
        self.__is_claw_cut = value

    @property
    def is_poil_long(self):
        return self.__is_poil_long
    
    @is_poil_long.setter
    def is_poil_long(self, value):
        self.__is_poil_long = value

    def se_decrire(self):
        if self.is_poil_long:
            poil = 'long'
        else:
            poil = 'court'
        if self.is_cut_griffe:
            griffes = 'coupées'
        else:
            griffes = 'non coupées'
        return f'{super(Chat, self).se_decrire()} les poils du chat sont: {poil} ces griffes sont : {griffes} il est  {self.caracter}'
