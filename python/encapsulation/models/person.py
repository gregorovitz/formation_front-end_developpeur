from datetime import datetime


class Person:
    def __init__(self, lastname: str, firstname: str, birthdate: datetime):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__birthdate = birthdate
    #     region Getter
    def get_firstname(self):
        return self.__firstname

    def get_lastname(self):
        return self.__lastname

    def get_birthdate(self):
        return self.__birthdate

    def get_birthdate_day(self):
        return self.get_birthdate().day

    def get_birthdate_month(self):
        return self.get_birthdate().month

    def get_birthdate_year(self):
        return self.get_birthdate().year
    # endregion

    # region setter

    def set_firstname(self,value):
        self.__firstname=value

    def set_lastname(self,value):
        self.__lastname =value

    def set_birthdate(self,value):
        self.__birthdate=value

    # endregion

    # region Propriete

    lastname=property(get_lastname,set_lastname)
    firstname=property(get_firstname,set_firstname)
    birthdate=property(get_birthdate,set_birthdate)
    birthdate_day=property(get_birthdate_day)
    birthdate_month = property(get_birthdate_month)
    birthdate_year = property(get_birthdate_year)

    # endregion



    def se_decrire(self):
        return "{} {} - {}/{}/{}".format(self.get_lastname(), self.get_firstname(), self.get_birthdate_day(), self.get_birthdate_month(),
                                         self.get_birthdate_year())
