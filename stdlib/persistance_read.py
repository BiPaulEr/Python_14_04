import os

directory = os.path.dirname(__file__)
file_name = "bibliotheque.dict"
path = os.path.join(directory, file_name)

import pickle

with open(path, "rb") as file:
    livres = pickle.load(file)

print(livres)