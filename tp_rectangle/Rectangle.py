
class Rectangle:
    cpt = 0
    def __init__(self,longueur,largeur):
        self.longueur = longueur
        self.largeur = largeur
        Rectangle.cpt+=1

    def get_surface(self):
        return self.longueur*self.largeur

    def __str__(self):
        return "Rectangle : {}, {}".format(self.longueur,self.largeur)