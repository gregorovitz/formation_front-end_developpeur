from datetime import datetime


class Stagiaire:
    def __init__(self, name: str, firstname: str, birthdate: datetime, is_smoker=False):
        self.__name = name
        self.__firstname = firstname
        self.__birthdate = birthdate
        self.__is_smoker = is_smoker

        # region getter
    @property
    def lastname(self):
        return self.__name

    @property
    def firstname(self):
        return self.__firstname

    @property
    def birthdate(self):
        return self.__birthdate

    @property
    def age(self):
        today = datetime.now()
        _age = today.year - self.birthdate.year
        if today.month < self.birthdate.month \
                or (today.month == self.birthdate.month and today.day < self.birthdate.day):
            _age -= 1
        return _age

    # endregion
    # region setter
    @lastname.setter
    def lastname(self, value):
        self.__name = value

    @firstname.setter
    def firstname(self, value):
        self.__firstname = value

    @birthdate.setter
    def birthdate(self, value):
        self.__birthdate = value

    #     endregion

    # region property

    # endregion
    def se_decrire(self):
        return "  {}  {} {} ".format(self.lastname, self.firstname, self.birthdate)

    def donne_nom_prenom(self):
        return"  {}  {}".format(self.lastname, self.firstname)

    def __str__(self):
        return f"Etudiant :{self.firstname} {self.lastname}"

    def __eg__(self, other):
        return self.firstname == other.firstname and self.lastname == other.lastname


