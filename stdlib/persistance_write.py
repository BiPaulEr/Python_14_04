import os

directory = os.path.dirname(__file__)
file_name = "bibliotheque.dict"
path = os.path.join(directory, file_name)

livres = [
    {"titre": "Les Misérables", "auteur": "Victor Hugo", "annee_publication": 1862},
    {"titre": "Le Petit Prince", "auteur": "Antoine de Saint-Exupéry", "annee_publication": 1943},
    {"titre": "Candide", "auteur": "Voltaire", "annee_publication": 1759},
]

import pickle

with open(path, "wb") as file:
    pickle.dump(livres, file)