def repetetion(nombre):
    def decorateur(function):
        def wrapper(*args, **kwargs):
            for _ in range(0, nombre):
                function(*args, **kwargs)
        return wrapper
    return decorateur

@repetetion(5)
def function_simple(a = 3):
    print("Je suis la fonction simple")

function_simple(a = 8)

@repetetion(1000)
def function_moins_simple(nom):
    print("Je suis la fonction simple", nom)

function_moins_simple("QUOI")