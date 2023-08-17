print("Welcome to python pizza Deliverys")

size = input("Quelle taille de pizza souhaiter-vous ? 'S' pour la petite, 'M' pour la moyenne, 'L' la grande :")

if size not in ['S', 'M', 'L','s','m','l']:

    print("veuillez choisir entre 'S' pour la  petite, 'M' pour la moyenne, 'L' pour la grande   ")
    exit()


add_pepperoni = input("Voullez-vous ajouter du pepperoni ? (oui/non) :")

extra_cheese = input("voulez-vous ajouter du fromage? (oui/non) :")


if size == "S":
    cout_total = 15
elif size == "M":
    cout_total = 20
else:
    cout_total = 25

if add_pepperoni == "oui":
    if size == "S" or size == "M":
        cout_total += 2
    else:
        cout_total += 3
if extra_cheese == "oui":
    cout_total += 1

print(f" votre facture s'élève à ${cout_total}. savourez votre pizza ")


