import argparse

livres = [
    {"titre": "Les Misérables", "auteur": "Victor Hugo", "annee_publication": 1862},
    {"titre": "Le Petit Prince", "auteur": "Antoine de Saint-Exupéry", "annee_publication": 1943},
    {"titre": "Candide", "auteur": "Voltaire", "annee_publication": 1759},
]

parser = argparse.ArgumentParser(description="Bibliotheque")
subparser = parser.add_subparsers(dest="command", description="Action à faire")

add_parser = subparser.add_parser("add", help ="Ajouter un tritre")
add_parser.add_argument("titre", type=str, help="Titre")
add_parser.add_argument("--auteur", type=str, default="Auteur Inconnue", help="Auteur")
add_parser.add_argument("--annee", type=int, default=-999999, help="Anne")

look_parser = subparser.add_parser("look", help ="Chercher un livre")
look_parser.add_argument("mode", choices=["titre", "auteur", "annee_publication"], type=str, help="Titre")
look_parser.add_argument("valeur", type=str, help="Titre")

args = parser.parse_args()
titres = list(map(lambda x : x["titre"], livres))

if args.command == "add":
    if args.titre in titres:
        print("Book already in the biblio")
    else:
        livres.append( {"titre": args.titre, "auteur": args.auteur, "annee_publication": args.annee})
else:
    liste_regarder = list(map(lambda x : str(x[args.mode]), livres))
    if args.valeur in liste_regarder:
        index = liste_regarder.index(args.valeur)
        print(livres[index])
    else:
        print("Pas de tritre")

print(livres)