class Formateur:
    def __init__(self, lastname: str, firstname: str, matiere: str):
        self.__lastname = lastname
        self.__firstname = firstname
        self.__matiere = matiere
    # region getter

    def get_lastname(self):
        return self.__lastname

    def get_firstname(self):
        return self.__firstname

    def get_matierre(self):
        return self.__matiere
    # endregion
    # region setter

    def set_lastname(self, value):
        self.__lastname = value

    def set_firstname(self, value):
        self.__firstname = value

    def set_matierre(self, value):
        self.__matiere = value
    #     endregion

# region property
    lastname = property(get_lastname, set_lastname)
    firstname = property(get_firstname, set_firstname)
    matiere = property(get_matierre, set_matierre)
# endregion

    def se_decrire(self):
        return " {}  {} forme au {} ".format(self.lastname, self.firstname, self.matiere)

    def __str__(self):
        return f"Etudiant :{self.firstname} {self.lastname} {self.matiere}"
