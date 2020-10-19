# définition classe voiture
class Voiture:
    def __init__(self,marque, modele,couleur="noir"):
        self.couleur=couleur
        self.vitesse=0
        self.marque=marque
        self.modele=modele

    def accelerer(self, gain):
        self.vitesse += gain

    def freiner(self, gain):
        self.vitesse -= gain

    def se_decrire(self):
        return "{} {} ({})".format (self.marque,self.modele,self.couleur)

if __name__ =='__main__':
    print('salut je suis le fichier voiture')