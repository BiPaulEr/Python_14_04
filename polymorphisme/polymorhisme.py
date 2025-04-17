class Animal:
    def parler(self):
        return "Hoo!"
    
class Chien(Animal):
    def parler(self):
        return "Woof!"
      
class Oiseau(Animal):
    def parler(self):
        return"Cuicui" 
    
class Chat(Animal):
    def parler(self):
        return "Miaou!"
    
animaux = [Chien(), Chat(), Chien(), Animal(), Oiseau()]

def jouer(animaux):
    for animal in animaux:
        print(animal.parler())
    
jouer(animaux)