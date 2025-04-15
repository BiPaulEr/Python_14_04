elements = [0, None, 0.0, 5,  True, 0, 7]
trouve = False
element_a_trouve = 5

for element in elements:
    print(f'analyse de lélément {element}')
    if element == element_a_trouve:
        trouve = True
        break

if trouve:
    print('Au moins un élément évalue à True')
else:
    print('Tous les éléments évaluent à False')
