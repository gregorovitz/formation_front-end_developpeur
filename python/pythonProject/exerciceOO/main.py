from datetime import datetime

from models.formateur import Formateur
from models.room import Room
from models.stagiaire import Stagiaire
if __name__ == '__main__':

    stag1 = Stagiaire("Marquebreucq", "Emmanuel", datetime(1991, 4, 4))
    stag2 = Stagiaire("De Jarmac", "Quentin", datetime(1991, 4, 4))
    stag3 = Stagiaire("Serck", "David", datetime(1991, 4, 4))
    stag4 = Stagiaire("Corbisier", "Sébastien", datetime(1991, 4, 4))
    stag5 = Stagiaire("Doyle", "Kévin", datetime(1991, 4, 4))
    stag6 = Stagiaire("test", "depassement", datetime(1991, 4, 4))
    formateur = Formateur("Strimelle", "Aurelien", "python")
    stag7 = Stagiaire("Nedostoupof", "Cédric", datetime(1991, 4, 4))
    stag8 = Stagiaire("Decker", "james", datetime(1991, 4, 4))
    stag9 = Stagiaire("Dhoore", "Roman", datetime(1991, 4, 4))
    stag10 = Stagiaire("Libert", "Maverick", datetime(1991, 4, 4))
    stag11 = Stagiaire("Espana Ribera", "Nicolas", datetime(1998, 12, 11))
    stag12 = Stagiaire("test", "depassement", datetime(1991, 4, 4))
    room = Room("114", 5, formateur)
    room2 = Room("115", 6, formateur)
    room.add_stagiaire(stag1)
    room.add_stagiaire(stag2)
    room.add_stagiaire(stag3)
    room.add_stagiaire(stag4)
    room.add_stagiaire(stag5)
    room.add_stagiaire(stag6)
    room2.add_stagiaires(stag7, stag8, stag9, stag10, stag11, stag12)

    print(room.se_decrire())
    print(room2.se_decrire())

    print(stag11.age)