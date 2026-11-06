import math

electrique = input("Le véhicule est-il électrique ? (oui/non) : ")
electrique = electrique.lower()

duree = float(input("Combien d'heures avez-vous stationné ? "))

if duree < 0:
    print("Erreur : la durée ne peut pas être négative.")

elif electrique != "oui" and electrique != "non":
    print("Erreur : entrez oui ou non.")

else:
    heures_facturees = math.ceil(duree)

    if heures_facturees == 0:
        prix = 0
    else:
        prix = 4 + (heures_facturees - 1) * 2.50

    if prix > 20:
        prix = 20

    if electrique == "oui":
        rabais = prix * 0.20
    else:
        rabais = 0

    total = prix - rabais

    print("Durée :", duree, "heures")
    print("Heures facturées :", heures_facturees)
    print("Prix avant rabais : $", round(prix, 2))
    print("Rabais véhicule électrique : $", round(rabais, 2))
    print("Total : $", round(total, 2))