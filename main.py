import math

def pythagoras(a, b):
    return math.sqrt(a**2 + b**2)

# Eingabe und Berechnung
a = float(input("Gib a ein: "))
b = float(input("Gib b ein: "))
print("Hypotenuse c:", pythagoras(a, b))
input('Drücke Enter zum Beenden')
