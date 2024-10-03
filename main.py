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
    return 2 + math.pi * kU
kU = float(input('Gib den Radius ein: '))
print('Der Umfang ist: ', umfang_kreis(kU))

def zylinder_volumen(rZ: float, h: float):
    return math.pi * (rZ * rZ) * h
rZ = float(input('Gib den Radius des Zylinders ein: '))
h= float(input('Gib die Höhe des Zylinder an: '))
print('Der Zylinder hat ein Volumen von: ', zylinder_volumen(rZ, h))

def Weg(speed: float, time: float):
    return speed * time
speed = float(input('Die Geschwindigkeit ist: '))
time = float(input('Wie lange dauerte es: '))
print('Der Weg ist: ', Weg(speed, time))



input()
