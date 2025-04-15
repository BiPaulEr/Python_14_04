def afficher_prix_total(prix_entree, prix_plat_principale,*args, prix_desert = 10, **kwargs):
    print(f"prix_desert {prix_desert}")
    somme = prix_entree + prix_plat_principale + prix_desert + sum(args)
    print(f"Prix du repas est {somme}")
    print(kwargs)

prix_commande = (5, 7, 9)
details_command_arg = {"client":'John Doe', "table":5, "alergie":'sans gluten'}
afficher_prix_total(10 , 13, 10, *prix_commande, **details_command_arg)
afficher_prix_total(10 , 13, *prix_commande)