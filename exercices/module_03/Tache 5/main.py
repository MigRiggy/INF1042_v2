age = 20
a_un_billet = True

acces_autorise = age >= 18 and a_un_billet

print(acces_autorise)
note = 85

if 0 <= note <= 100:
    print("Note valide")
else:
    print("Note invalide")
taille = 135
age = 13
a_interdiction = False

if (taille >= 140 or age >= 12) and not a_interdiction:
    print("Accès permis")
else:
    print("Accès refusé")
age = 20
est_etudiant = True

if age >= 18 and est_etudiant:
    print("Tarif étudiant disponible")
else:
    print("Plein tarif")
age = 25

if age < 13:
    print("Enfant")
elif age <= 17:
    print("Adolescent")
elif age <= 64:
    print("Adulte")
else:
    print("Aîné")