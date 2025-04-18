class TailleInvalideException(Exception):
    pass

def convertir_en_entier(chaine):
    if not isinstance(chaine, str):
        raise TypeError(f"{chaine} is not str -> is {type(chaine)}")
    if len(chaine) < 5:
        raise TailleInvalideException(f"{len(chaine)} not enough long")
    try:
        result = int(chaine)
    except ValueError as ve:
        print(f"{ve}")
        return 0
    else:
        return result
    finally:
        print("Fin de la conversion")

try:
    print(convertir_en_entier("3000000"))

    print(convertir_en_entier("3.5"))
    print(convertir_en_entier([]))
except TypeError as te:
    print(f"{te}")
except Exception as e:
    print(f"{e}")

print("end")