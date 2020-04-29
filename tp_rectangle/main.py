
from Rectangle import Rectangle

if __name__ == "__main__":
    r = Rectangle(largeur=2,longueur=12)
    r1 = Rectangle(largeur=12,longueur=65)
    r2 = Rectangle(largeur=22,longueur=78)

    print("longueur",r.longueur)
    print("largeur",r.largeur)
    surface = r.get_surface()
    print("surface",surface)

    print(r.cpt)
    print(r1.cpt)
    print(r2.cpt)


    