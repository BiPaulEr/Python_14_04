for i in range(20, 26):
    print(i ** 2)

somme = 0
for i in range(1, 51):
    if i % 2:
        somme = somme + i
print(somme)

somme = 0
for i in range(1, 50, 2):
    somme = somme + i
print(somme)

print(sum(range(1, 50, 2)))

chaine = "Bonjour Python"
"""
for i in range(len(chaine) - 1, -1, -1):
    #print(chaine[i])
for i in range(-1, - len(chaine) -1, -1):
    print(chaine[i])
for carac in reversed(chaine):
    print(carac)
"""

liste = [10, 9, 8, 7, 6, 5, 3, 2, 1, 0]
for index, valeur in enumerate(liste):
    print("index :", index, "valeur :", valeur)

