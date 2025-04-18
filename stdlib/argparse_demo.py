import argparse

parser = argparse.ArgumentParser(description="MA CLI")
parser.add_argument("nom", type=str, help="C'est ton nom de famille")
parser.add_argument("age", type=int, help="C'est ton age")
parser.add_argument("--crie", type=str, default="OUAH", help="Crie de raliment")

parser.add_argument('--verbose', action='store_true', help='Mode verbeux')

args = parser.parse_args()
print("nom", args.nom)
print("age", args.age)
print("crie", args.crie)

print(args.verbose)