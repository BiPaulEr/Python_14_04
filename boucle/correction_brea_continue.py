elements = ['pomme', 'banane', 'cerise', 'date', 'banane', 'baie']

deja_vu = []
for element in elements:
    if element in deja_vu:
        print("Element en double ", element)
        break
    print(element)
    deja_vu.append(element)