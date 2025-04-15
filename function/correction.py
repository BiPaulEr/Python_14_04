def calculer_prix_ttc(prix_ht, tva):
    prix_ttc = (1.0 + (tva / 100) ) * prix_ht
    return prix_ttc

print(calculer_prix_ttc(100, 20))
print(calculer_prix_ttc(100, 5))