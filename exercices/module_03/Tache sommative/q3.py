montant_initial = float(input("Entrez le montant avant taxes : $"))

if montant_initial < 50:
    pourcentage_rabais = 0
elif montant_initial <= 100:
    pourcentage_rabais = 5
else:
    pourcentage_rabais = 10

montant_economise = montant_initial * pourcentage_rabais / 100

sous_total = montant_initial - montant_economise

taxe = sous_total * 0.13

total_final = sous_total + taxe

print("Montant initial : $", round(montant_initial, 2))
print("Pourcentage de rabais :", pourcentage_rabais, "%")
print("Montant économisé : $", round(montant_economise, 2))
print("Sous-total après rabais : $", round(sous_total, 2))
print("TVH : $", round(taxe, 2))
print("Total final : $", round(total_final, 2))