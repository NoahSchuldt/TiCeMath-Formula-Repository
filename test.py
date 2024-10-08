import math
def geometrische_Gleichungen():
    print("geometrische Gleichnungen")

def logarythmen():
    print("logarythmen")

def warscheinlichkeiten_funktionen():
    print("warscheinlichkeiten und funktionen")

def Main_Menü():
    while True:
        print("\nMain_Menü:")
        print("1. geometrische_Gleichungen 1")
        print("2. logarythmen 2")
        print("3. warscheinlichkeiten_funktionen 3")
        print("4. Verlassen 4")
        auswahl = input("Bitte Option wählen: ")
        if auswahl == '1'
        (geometrische_Gleichungen)
        if auswahl == '2'
        (logarythmen)
        if auswahl == '3'
        (warscheinlichkeiten_funktionen)
        if auswahl == '4'
        break
else:
print("ungültige auswahl")

if __name__ == "__main__":
    obermenü()
        
def pythagoras():
    a = float(input("Gib a ein(cm): "))
    b = float(input("Gib b ein(cm): "))
    return math.sqrt(a**2 + b**2)   

def flaeche_kreis():
    r = float(input('Gib den Radius des Kreises ein(cm): '))
    return math.pi * r**2
def umfang_kreis():
    kU = float(input('Gib den Radius ein(cm): '))
    return 2 + math.pi * kU



def zylinder_volumen():
    rZ = float(input('Gib den Radius des Zylinders ein(cm): '))
    h= float(input('Gib die Höhe des Zylinder an(cm): '))
    return math.pi * (rZ * rZ) * h



def Weg():
    search = str(input("Was möchtest du berechnen?\nZeit, Weg oder Geschwindigkeit)"))
    if search=="Weg":
        speed = float(input('Die Geschwindigkeit ist(m/s): '))
        time = float(input('Wie lange dauerte es(s): '))
        print('Der Weg ist(m): ',speed * time)
    elif search=="Zeit":
        speed=float(input('Die Geschwindigkeit ist(m/s): '))
        distance=float(input('Der Weg ist(m):'))
        print('Die Zeit ist(s): ',distance/speed)
    else:
        time = float(input('Wie lange dauerte es(s): '))
        distance=float(input('Der Weg ist(m):'))
        print('Die Geschwindigkeit ist(m/s): ',distance/time)

def kegel_oberfläche():
    rK = float(input('Gib den Radius der Grundfläche des Kegels an: '))
    sK = float(input('Gib die Seitenlänge des Kegels an: '))
    return rK * math.pi * (rK * sK)

#Gibt die Optionen weiter an den User
print ("[1]Hypotenuse\n[2]Kreisfläche\n[3]Kreisumfang\n[4]Zylindervolumen\n[5]Distanzumrechnungen\n[6]Kegeloberfläche")

answer = int(input("Welche Option?\n"))
if answer==1:
    print("Hypotenuse c(cm):", pythagoras())
elif answer==2:
    print('Der Flächeninhalt des Kreises ist(cm²):', flaeche_kreis())
elif answer==3:
    print('Der Umfang ist(cm): ', umfang_kreis())
elif answer==4:
    print('Der Zylinder hat ein Volumen von(cm³): ', zylinder_volumen())
elif answer==5:
    Weg()
elif answer==6:
    print('Die Oberfläche des Kegels ist: ', kegel_oberfläche())
