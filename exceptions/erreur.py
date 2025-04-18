import random as r

def f1(liste):
    liste.append("f1")
    if r.randint(1, 100) > 80:
        return None
    return liste

def f2(liste):
    liste.append("f2")
    if r.randint(1, 100) > 80:
        return None
    return liste

def f3(liste):
    liste.append("f3")
    if r.randint(1, 100) > 80:
        return None
    return liste

def f4(liste):
    liste.append("f4")
    if r.randint(1, 100) > 80:
        return None
    return liste

liste = []
liste = f1(liste)
if liste:
    liste = f2(liste)
    if liste:
        liste = f3(liste)
        if liste:
            liste = f4(liste)

print(liste)