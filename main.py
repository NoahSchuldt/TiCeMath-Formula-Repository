import math

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
overmenu=int(input('[1]Mathematik\n[2]Physik'))
if overmenu==1:
    print ("[1]Hypotenuse\n[2]Kreisfläche\n[3]Kreisumfang\n[4]Zylindervolumen\n[5]Distanzumrechnungen\n[6]Kegeloberfläche\n[0]Programm beeenden")

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
    elif answer==0:
        print()
elif overmenu==2:
    print('[1]Elektrischer Strom\n[0]Programm beenden')
    phy = int(input('Welche Option'))
