import math

def pythagoras(a, b):
    return math.sqrt(a**2 + b**2)
    
a = float(input("Gib a ein: "))
b = float(input("Gib b ein: "))
print("Hypotenuse c:", pythagoras(a, b))

def flaeche_kreis(r):
    return math.pi * r**2

r = float(input('Gib den Radius des Kreises ein: '))
print('Der Flächeninhalt des Kreises ist:', flaeche_kreis(r))

def umfang_kreis(rU):
    return 2 + math.pi * rU

rU = float(input('Gib den Radius ein: '))
print('Der Umfang ist: ', umfang_kreis(rU))


input()
