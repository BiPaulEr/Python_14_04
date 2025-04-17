class Person():
    atrtibut_de_classe = "78"

    def __init__(self, prenom, nom):
        self.prenom = prenom
        self.nom = nom
    
    def print(self):
        print("Salut, je suis", self.prenom, self.nom)

pers1 = Person("Paul", "Martin")
print(pers1)
pers1.print()
Person.print(pers1)

chaine = str("ok")
chaine.upper()

pers2 = Person("Ernest", "Dupont")
pers2.print()

Person.nouvelle_methode = lambda self : print(f"JE SUIS LE ROI {self.nom}")
pers1.nouvelle_methode() #JE SUIS LE ROI Martin