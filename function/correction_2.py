liste = [5, 15, None, 10, 20] 

def nettoyer_donnees(liste):
    return_liste = []
    for element in liste:
        if (element != None):
            return_liste.append(element)
    return return_liste

def filter_donnees(liste):
    return_liste = []
    for element in liste:
        if element <= 10 and element >= 0:
            return_liste.append(element)
    return return_liste

def analyser_donnes(liste):
    return filter_donnees(nettoyer_donnees(liste))

liste_nettoye = nettoyer_donnees(liste)
liste_filtre = filter_donnees(liste_nettoye)
liste_nettoye_filtre = analyser_donnes(liste)
print(liste)
print(liste_nettoye)
print(liste_filtre)
print(liste_nettoye_filtre)