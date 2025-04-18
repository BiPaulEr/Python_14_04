import os
directory = os.path.dirname(__file__)
file_name = "data.txt"
path = os.path.join(directory, "data", file_name)

file = open(path, "rt")
try:
    for ligne in file.readlines():
        print(ligne.rstrip())
except Exception as e:
    print(f"{e}")
finally:
    file.close() 

with open(path, "rt") as file:
    for ligne in file.readlines():
        print(ligne.rstrip())