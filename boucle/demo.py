prenoms = ["Paul", "Martin", "", "Axel", ""]
noms = ["Lefebre", "Dupont", "Aigouy"]
nationalites =["fr"]*3

for index, (prenom, nom, nation) in enumerate(zip(prenoms, noms, nationalites)):
    print(prenom, nom, nation)
    prenoms[index] = prenom.upper()

print(prenoms)
