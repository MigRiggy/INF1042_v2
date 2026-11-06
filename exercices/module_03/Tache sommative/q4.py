import random

nombre_tirages = int(input("Combien de tirages voulez-vous effectuer ? "))

while nombre_tirages <= 0:
    print("Entrez un nombre supérieur à 0.")
    nombre_tirages = int(input("Combien de tirages voulez-vous effectuer ? "))

compteur_1 = 0
compteur_2 = 0
compteur_3 = 0
compteur_4 = 0

for i in range(nombre_tirages):
    resultat = random.randint(1, 4)

    if resultat == 1:
        compteur_1 += 1
    elif resultat == 2:
        compteur_2 += 1
    elif resultat == 3:
        compteur_3 += 1
    else:
        compteur_4 += 1

pourcentage_1 = compteur_1 / nombre_tirages * 100
pourcentage_2 = compteur_2 / nombre_tirages * 100
pourcentage_3 = compteur_3 / nombre_tirages * 100
pourcentage_4 = compteur_4 / nombre_tirages * 100

print("Résultats :")
print("1 :", compteur_1, "fois -", round(pourcentage_1, 2), "%")
print("2 :", compteur_2, "fois -", round(pourcentage_2, 2), "%")
print("3 :", compteur_3, "fois -", round(pourcentage_3, 2), "%")
print("4 :", compteur_4, "fois -", round(pourcentage_4, 2), "%")

plus_frequent = max(compteur_1, compteur_2, compteur_3, compteur_4)

print("Nombre(s) tiré(s) le plus souvent :")

if compteur_1 == plus_frequent:
    print("1")
if compteur_2 == plus_frequent:
    print("2")
if compteur_3 == plus_frequent:
    print("3")
if compteur_4 == plus_frequent:
    print("4")