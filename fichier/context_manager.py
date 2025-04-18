class ContextIllustration:
    def __init__(self, nom):
        self.nom = nom
    def __enter__(self):
        print("Je suis en train de rentrer dans le contexte")
        return self.nom * 5

    def __exit__(self, exc_type, exc, tb):
        print("Je suis dans le exit")
        if exc_type:
            print(f"Exception Detected : {exc_type} {exc}")
        return True
    
with ContextIllustration("Dog") as variable:
    print(variable)
    print("Je suis dans le contexte")
    #raise Exception("QUOI")
    print("Je suis dans le contexte")


print("end")