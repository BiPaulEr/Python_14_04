class Person():
    def __init__(self, public, protege, private):
        self.attribut_public = public
        self._attribut_protege = protege
        self.__attribut_private = private
    
    def methode_public(self):
        print("methode ", self.__attribut_private)
    
    def _methode_protected(self):
        print("methode ", self.__attribut_private)

    def __methode_private(self):
        print("methode ", self.__attribut_private)

pers1 = Person("PUBLIC", "PROTECTED", "PRIVATE")
print(pers1.attribut_public)
print(pers1._attribut_protege)
#print(pers1.__attribut_private) # ATTRIBUT ERROR

print(pers1._Person__attribut_private)
pers1.methode()