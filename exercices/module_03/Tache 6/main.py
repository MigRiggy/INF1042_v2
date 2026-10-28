nom = input("Entre ton nom : ")

if 8 <= len(nom) <= 12:
    print("Nom valide.")
else:
    print("Erreur : ton nom doit contenir entre 8 et 12 caractères.")
nom = input("Entre ton nom : ")
age = int(input("Entre ton âge : "))

print(f"{nom}, dans 5 ans, tu auras {age + 5} ans.")
nombre1 = float(input("Entre le premier nombre décimal : "))
nombre2 = float(input("Entre le deuxième nombre décimal : "))

produit = nombre1 * nombre2
difference = nombre1 - nombre2

print("Le produit est :", produit)
print("La différence est :", difference)
