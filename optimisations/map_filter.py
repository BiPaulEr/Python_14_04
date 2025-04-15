liste = [5, 15, None, 10, 20] 

liste_filtre = list(map(lambda x : x*2, filter(lambda element: (element is not None) and (0<=element<=10), liste)))

print(liste_filtre)


liste_fitre2 = [element*2 for element in liste if (element is not None) and (0<=element<=10)]
print(liste_fitre2)