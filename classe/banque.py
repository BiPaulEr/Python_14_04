class Compte():
    def __init__(self, compte):
        self.__compte = compte
    
    def __operation(self, montant):
        self.__compte += montant
    
    def printCompte(self):
        print(self.__compte)
    
    
compte = Compte(1000)
#print(compte._Compte__compte)
compte.printCompte()
