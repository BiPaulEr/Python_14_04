class Voiture:
    def __init__(self, marque, modele):
        self.marque = marque
        self.modele = modele
        
    def description(self):
        return f"Je suis une voiture {self.marque} {self.modele}"

class VoitureSport(Voiture):
    def __init__(self, vitesse_max, marque, modele):
        super().__init__(marque, modele)
        self.vitesse_max = vitesse_max

    def description(self):
        msg = super().description()
        return f"{msg} avec une vitesse de {self.vitesse_max}"

voiture = Voiture("Peugeot", "Parnet")
print(voiture.description())

voiture_sport = VoitureSport("230", "Peugeot", "RCZ")
print(voiture_sport.description())