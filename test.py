import math
#das ist eine Tesfunktion die ich daheimweitermache nicht editen!
def gleichungskürzer():
    gleichung=input("Gib die Gleichung f(x) ein")
    Elemente=[]
    Stack=[]
    for symbol in gleichung:
        if symbol == '1' or symbol == '2' or symbol == '3' or symbol == '4' or symbol == '5' or symbol == '6' or symbol == '7' or symbol == '8' or symbol == '9' or symbol == '0':
            Stack.append(symbol)
            print(3)
        else:
            if Stack != []:
                int_result = int(''.join(map(str, Stack)))
                Elemente.append(int_result)
                Stack = []
            Elemente.append(symbol)
    if Stack != []:
        int_result = int(''.join(map(str, Stack)))
        Elemente.append(int_result)
    print (Elemente)
    DivisionsZähler = 1

    def Divisionskürzer(Term_List, Counter):
        Nenner=False
        Divisionspunkt = 0
        for Suche in Term_List:
            if Suche == "/":
                break
            else:
                DivLocation += 1
        InRechnung = True
        Suchpunkt = DivisionsZähler
        if Nenner == False:
            KlammerLayer = 0
            while InRechnung:
                if Term_List(Suchpunkt) == ')'
                    KlammerLayer += 1
                    

    
    def therme_und_gleichungen():
        print("therme_und_gleichungen")

def funktionen():
    print("funktionen")

def geometrie():
    print("geometrie")

def wahrscheinlichkeiten():
    print("wahrscheinlichkeiten")

def obermenü():
    while True:
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
