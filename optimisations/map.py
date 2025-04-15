liste = ["paul", "ernest", "martin"]

liste_upper2 = list(map(lambda element: element.upper(), liste))
print(liste_upper2)

liste_capitalize2 = list(map(lambda element: element.capitalize(), liste))
print(liste_capitalize2)

liste_upper = []
for element in liste:
    liste_upper.append(element.upper())
print(liste_upper)

liste_capitalize = []
for element in liste:
    liste_capitalize.append(element.capitalize())
print(liste_capitalize)
