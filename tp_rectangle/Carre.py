from Rectangle import Rectangle


class Carre(Rectangle):
    

    def __init__(self,cote):
        super().__init__(cote,cote)
        self.cote = cote

    def __str__(self):
        return "Carre : {}".format(self.cote)

    def set_altitude(alt)