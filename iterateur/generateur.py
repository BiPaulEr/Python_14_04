def generateur(fin):
    print("Debut generateur")
    for i in range(0, fin):
        yield i 
        print("Apres le yield")
    print("End generateur")

""" 
gen = generateur(5)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
"""
gen = generateur(5)
for valeur in gen:
    print(valeur)
for valeur in gen:
    print(valeur)

print("end")