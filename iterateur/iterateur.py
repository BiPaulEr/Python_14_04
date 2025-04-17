class CompteurIterable:
    def __init__(self):
        self.compteur = 10
    def __iter__(self):
        return Compteur(self.compteur)

class Compteur:
    def __init__(self, compteur):
        self.compteur = compteur

    def __next__(self):
        if self.compteur < 0:
            raise StopIteration
        self.compteur = self.compteur - 1
        return self.compteur

compteur = CompteurIterable()

for i in compteur:
    print(i)

for i in compteur:
    print(i)