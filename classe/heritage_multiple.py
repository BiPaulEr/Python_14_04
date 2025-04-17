class Base:
    def __init__(self, valeur_base):
        self.valeur_base = valeur_base
        print("Base init " + self.valeur_base)

class A(Base):
    def __init__(self, valeur_a, *args):
        super().__init__(*args)
        self.valeur_a = valeur_a
        print("A init " + self.valeur_a)

class B(Base):
    def __init__(self, valeur_b, *args):
        super().__init__(*args)
        self.valeur_b = valeur_b
        print("B init "  + self.valeur_b)

class C(A, B):
    def __init__(self, valeur_a, valeur_b, valeur_base):
        super().__init__(valeur_a, valeur_b, valeur_base)
        print("C init")

c = C("GRAND A", "GRAND B", "BASE VALUE")
