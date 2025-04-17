from abc import ABC, abstractmethod

class Instrument(ABC):
    @abstractmethod
    def jouer(self):
        pass

class Guitare(Instrument):
    def jouer(self):
        print("Dring")

class Piano(Instrument):
    def jouer(self):
        print("Piout")

class Batterie(Instrument):
    def jouer(self):
        print("Boom")    

def faire_jouer(liste_instrument):
    for instrument in liste_instrument:
        instrument.jouer()

instru = Instrument()

liste_instrument = [Guitare(), Piano(), Batterie()]

faire_jouer(liste_instrument)