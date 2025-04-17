def decorateur(function):
    def wrapper(*args, **kwargs):
        print("Ajout d'instruction avant")
        function(*args, **kwargs)
        print("Ajout d'instruction apres")
    return wrapper

@decorateur
def function_simple(a = 3):
    print("Je suis la fonction simple")

function_simple(a = 8)

@decorateur
def function_moins_simple(nom):
    print("Je suis la fonction simple", nom)

function_moins_simple("QUOI")