import random as r

def f4(liste):
    liste.append("f4")
    if r.randint(1, 100) > 20:
        raise Exception("F4")
    return liste

def f3(liste):
    liste.append("f3")
    if r.randint(1, 100) > 80:
        raise Exception("F3")
    return f4(liste)

def f2(liste):
    liste.append("f2")
    if r.randint(1, 100) > 80:
        raise Exception("F2")
    try:
        liste = f3(liste)
    except Exception as e:
        print(f"F2 !!! -> {e}")
    return liste

def f1(liste):
    liste.append("f1")
    if r.randint(1, 100) > 80:
        raise Exception("F1")
    return f2(liste)



liste = []
try: 
    liste = f1(liste)
except Exception as e:
    print(f"{e}")
    if hasattr(e, "quoi"):
        print(getattr(e, "quoi"))

print(liste)