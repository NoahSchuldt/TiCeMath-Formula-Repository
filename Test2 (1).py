import math
#das ist eine Tesfunktion die ich daheimweitermache nicht editen!
def gleichungskürzer():
    gleichung=input("Gib die Gleichung f(x) ein")
    gleichungskomponenten=[gleichung]
    print (gleichung)
def therme_und_gleichungen():
    print("therme_und_gleichungen")

def funktionen():
    print("funktionen")

def geometrie():
    print("geometrie")

def wahrscheinlichkeiten():
    print("wahrscheinlichkeiten")

def obermenü():
    
        print("\nObermenü:")
        print("1. therme_und_gleichungen 1")
        print("2. fuktionen 2")
        print("3. geometrie 3")
        print("4. wahrscheinlichkeiten 4")

auswahl = input("Bitte wählen")

if auswahl == '1':
    therme_und_gleichungen()

elif auswahl == '2':
    funktionen()

elif auswahl == '3':
    geometrie()

elif auswahl == '4':
    wahrscheinlichkeiten()

else:
    print:("ungültige auswahl")

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

#gerader Kreiskegel ab hier! Hier arbeitet annabelle bitte nicht verändern Danke 
def volumen_gerader_kreiskegel():
    r = float(input("Gib den Radius des Kreises ein(cm): "))
    h = float(input("Gib die Höhe des Kreises an(cm): "))
    return 1, 3 * r**2 + math.pi * h

def mantel_gerader_kreiskegel():
    r = float(input("Gib den Radius des Kreiskegels ein(cm): "))
    s = float(input("Gib die Seitenlänge des Kreiskegels ein(cm): "))
    return r * math.pi * s

def oberflaeche_gerader_kreiskegel():
    r = float(input("Gib den Radius des Kreises ein(cm): "))
    s = float(input("Gib die Seitenlänge des Kreiskegels ein(cm): "))
    return r * math.pi * (r+s)

#Mantelpunktswinkel der Mantelfläche


#ende Kreiskegel

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
