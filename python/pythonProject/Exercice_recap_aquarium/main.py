from model.algue import Algue
from model.aquarium import Aquarium
from model.merou import Merou

from model.sole import Sole

if __name__ == '__main__':



    aquarium=Aquarium('aqua')

    poisson1=Merou ('poisson1', 'f')
    poisson2=Sole('poisson2','m')
    poisson3=Sole('poisson3','f')
    poisson4=Merou('poisson4','m')
    algue1=Algue()
    aquarium.add_poisson(poisson1)
    aquarium.add_poisson(poisson2)
    aquarium.add_poisson(poisson3)
    aquarium.add_poisson(poisson4)
    aquarium.add_algue(algue1)
    while len(aquarium.poissons)>0 :
        input()
        print(aquarium.new_year())
