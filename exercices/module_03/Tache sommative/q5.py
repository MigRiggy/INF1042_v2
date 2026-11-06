import random

victoires = 0
defaites = 0
egalites = 0

choix_possibles = ["pierre", "papier", "ciseaux"]

while True:
    joueur = input("Choisissez pierre, papier, ciseaux ou quitter : ")
    joueur = joueur.lower()

    if joueur == "quitter":
        break

    if joueur not in choix_possibles:
        print("Choix invalide. Essayez encore.")
        continue

    ordinateur = random.choice(choix_possibles)

    print("Votre choix :", joueur)
    print("Choix de l'ordinateur :", ordinateur)

    if joueur == ordinateur:
        print("Égalité !")
        egalites += 1

    elif (joueur == "pierre" and ordinateur == "ciseaux") or \
         (joueur == "ciseaux" and ordinateur == "papier") or \
         (joueur == "papier" and ordinateur == "pierre"):
        print("Vous avez gagné !")
        victoires += 1

    else:
        print("Vous avez perdu !")
        defaites += 1

    print()

total_parties = victoires + defaites + egalites

print("Résultats finaux :")
print("Victoires :", victoires)
print("Défaites :", defaites)
print("Égalités :", egalites)
print("Total de parties :", total_parties)