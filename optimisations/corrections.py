noms = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

etudiants = list(zip(noms, scores))
print(etudiants) #[('Alice', 85), ('Bob', 92), ('Charlie', 78)]

etudiants_20 = list(map(lambda x : (x[0], x[1]  / 5), etudiants))
print(etudiants_20) #[('Alice', 17.0), ('Bob', 18.4), ('Charlie', 15.6)]

etudiants_sup_17 = list(filter(lambda x : x[1] >= 17, etudiants_20))
print(etudiants_sup_17) #[('Alice', 17.0), ('Bob', 18.4)]

notes_sup_17 = list(map(lambda x : x[1], etudiants_sup_17))
print(notes_sup_17) #[17.0, 18.4]

print(sum(notes_sup_17) / len(notes_sup_17)) #17.7

etudiants_sup_17_com = [(etudiant, note / 5) for etudiant, note in etudiants if note >= (17 * 5)]
print(etudiants_sup_17_com)