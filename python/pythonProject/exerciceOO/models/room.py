
from models.formateur import Formateur


class Room:
    def __init__(self, name: str, nbr_place, formateur: Formateur):
        self.__name = name
        self.__nbr_place = nbr_place
        self.__stagiaires = []
        self.__formateur = formateur
    #     region get

    def get_name(self):
        return self.__name

    def get_nbr_place(self):
        return self.__nbr_place

    def get_stagiaire(self):
        return tuple(self.__stagiaires)

    def get_formateur(self):
        return self.__formateur

    # endregion

    # region set
    def set_name(self, value):
        self.__name = value

    def set_formateur(self, value):
        self.__formateur = value
    # endregion
    # region property
    name = property(get_name, set_name)
    stagiaires = property(get_stagiaire)
    formateur = property(get_formateur, set_formateur)
    nb_place = property(get_nbr_place)
    # endregion

    def add_stagiaire(self, value):
        if len(self.stagiaires) < self.nb_place:
            self.__stagiaires.append(value)
        else:
            raise ValueError("trop d'etudiant !")

    def add_stagiaires(self, *students):

        for student in range(len(students)):
            self.add_stagiaire(student)

    def se_decrire(self):
        return"le formateur {} :\n {}dans la salle {} ".format(self.formateur.se_decrire(), self.afficher_stagiaire(),
                                                               self.name)

    def afficher_stagiaire(self):
        nom_prenom_stagiaire = ''
        for i in range(len(self.stagiaires)):
            nom_prenom_stagiaire = nom_prenom_stagiaire+self.stagiaires[i].donne_nom_prenom()+'\n '
        return nom_prenom_stagiaire
