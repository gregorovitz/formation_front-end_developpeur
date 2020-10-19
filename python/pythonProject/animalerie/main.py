from datetime import datetime

from models.animal import Animal
from models.animalerie import Animalerie
from models.chat import Chat
from models.chien import Chien
from models.oiseau import Oiseau




if __name__ == '__main__':
    monanimalerie=Animalerie()
    chat1 = Chat('minet', 5, 30, 'm', datetime(2015,2, 12), datetime.now(), "farouche")

    oiseau1 = Oiseau('bird', 15, 10, 'f', datetime(2018 , 12 , 12), datetime.now(), 'red')
    chien1 = Chien('dog', 15, 10, 'm', datetime(2018, 12, 12), datetime.now(), 'red','dog allemand')
    monanimalerie.add_animals(chat1, oiseau1, chien1)
    print(monanimalerie.affiche_animal())
    print(monanimalerie.nombre_animal())
    while monanimalerie.nb_animal>0:
        print ('simulation d\'une nuit')
        monanimalerie.nouvel_journee()
        print(monanimalerie.nombre_animal())
        print(monanimalerie.affiche_animal())

    print("game over!")