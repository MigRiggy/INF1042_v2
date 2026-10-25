note1 = 12
note2 = 15
note3 = 9

moyenne = (note1 + note2 + note3) / 3

print(f"Moyenne = {moyenne:.2f}")


secondes = 367

minutes = secondes // 60
reste = secondes % 60

print(f"{secondes} secondes = {minutes} min {reste} s")


prix = 3.99
taxe = 0.13

montant_taxe = prix * taxe
total = prix + montant_taxe

print(f"Taxe = {montant_taxe:.2f} $")
print(f"Total = {total:.2f} $")


x = 7.8

y = int(x)
diff = x - y

print(f"y = {y}")
print(f"diff = {diff}")


bonbons = 53
eleves = 8

part = bonbons // eleves
reste = bonbons % eleves

print(f"Chaque élève reçoit {part} bonbons.")
print(f"Il reste {reste} bonbons.")

print(f"53 / 8 = {bonbons / eleves}")