celsius = float(input("Entrez une température en Celsius : "))

if celsius < -273.15:
    print("Erreur : la température ne peut pas être inférieure à -273.15 °C.")
else:
    fahrenheit = (celsius * 9 / 5) + 32
    kelvin = celsius + 273.15

    print("Celsius :", round(celsius, 2), "°C")
    print("Fahrenheit :", round(fahrenheit, 2), "°F")
    print("Kelvin :", round(kelvin, 2), "K")