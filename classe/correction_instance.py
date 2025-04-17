class Person():
    def __init__(self, prenom, nom):
        self.prenom = prenom
        self.nom = nom
    
    def saluer(self):
        print("Salut, je suis", self.prenom, self.nom)

pers1 = Person("Alice", "Martin")
pers1.saluer()
pers1.private #bug


pers2 = Person("Pierre", "Dupont")
pers2.saluer()