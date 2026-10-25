age = int(input("Quel âge as-tu ? "))

if age >= 18:
    print("Accès autorisé")
else:
    print("Accès restreint")


mot_de_passe = input("Entre le mot de passe : ")

if mot_de_passe == "Boréal":
    print("Accès accordé")
else:
    print("Accès refusé")


note = int(input("Entre ta note : "))

if note >= 60:
    print("Réussite")
elif note >= 50:
    print("Rattrapage")
else:
    print("Échec")


nombre = int(input("Entre un nombre entier : "))

if nombre > 0 and nombre < 100:
    print("Nombre valide")
else:
    print("Nombre hors limite")


import random

choix = ["Pierre", "Papier", "Ciseaux"]
ordinateur = random.choice(choix)

utilisateur = input("Choisis Pierre, Papier ou Ciseaux : ")

print("L'ordinateur a choisi", ordinateur)

if utilisateur == ordinateur:
    print("Égalité !")
else:
    print("Choix différents !")