class Forme:
    def __init__(self, type_forme):
        self.type_forme = type_forme   
    def calculer_aire(self):
        return 0 

class Cercle(Forme):
    def __init__(self, rayon):
        super().__init__("Cercle")
        self.rayon = rayon 

    def calculer_aire(self):
        return 3.14 * self.rayon**2
    
class Rectangle(Forme):
    def __init__(self, longeur, largeur):
        super().__init__("Rectangle")
        self.longeur = longeur
        self.largeur = largeur
    
    def calculer_aire(self):
        return self.largeur * self.longeur
    
class Carre(Rectangle):
    def __init__(self, cote):
        super().__init__(cote, cote)

