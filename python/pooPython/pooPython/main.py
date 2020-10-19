from model.voiture import Voiture


if __name__ =='__main__':
    v1 = Voiture("VW", "polo", "vert Pomme")
    v2 = Voiture("Audi", "A4")
    print(v1)
    print(v2)
    print(v1.marque,v1.modele,v1.couleur)
    print(v2.marque, v2.modele, v2.couleur)
    print(v1.vitesse)
    v1.accelerer(100)
    print(v1.vitesse)
    v1.freiner(25)
    print(v1.vitesse)
    desc=v1.se_decrire()
    print(desc)