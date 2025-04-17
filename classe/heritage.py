class Animal:
    def __init__(self, nom):
        self.nom = nom

    def parler(self):
        return f"Je suis un animal {self.nom}"

class Chien(Animal):
    def __init__(self, race_de_chien, nom):
        self.race_de_chien = race_de_chien
        super().__init__(nom)

    def parler(self):
        return f"Je suis un {self.race_de_chien} WAOUF {self.nom}"

class Chat(Animal):
    def parler(self):
        msg = super().parler()
        return f"{msg}, Miaou"

class Ornitorinc(Animal):
    pass

animal = Animal("Oiseau")
chien = Chien("Labrador", "Rex")
chat = Chat("Mimi")
orni = Ornitorinc("DODO")

print(animal.nom, "dit :", animal.parler())
#Oiseau dit : Je suis un animal
print("dit :", chien.parler())
#Rex dit : Je suis un animal
print(chat.nom, "dit :", chat.parler())
#Chat dit : Je suis un animal