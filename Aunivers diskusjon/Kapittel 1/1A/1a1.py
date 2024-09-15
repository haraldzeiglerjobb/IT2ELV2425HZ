"""
En syklist rundt en bane
Hen sykler med 50 km/h rundt der i momentanfart

* Beregner banens lengde gitt at hen sykler midt på banen 
(kunne det vært mulig å gi input på hvor mange prosent ut fra
venstre eller høyre for eksempel? Der 50% tilsvarer midt i?)
* Beregner syklistens gjennomsnittsfart
* Beregner tiden syklisten bruker på 10 runder

"""
import math
v = 50      #km/h
v1 = 50/3.6 #m/s

#1a
def length_of_one_round(dist_from_center: float = 0.0):
    straight = 100.0
    curve = math.pi*(31.83+dist_from_center)
    return 2*(straight +curve)



def a():
    print(f"Lengden til en runde er {length_of_one_round(0):.3f} meter (m)")
    

#1b
def b():
    print(f"Hastigheten er {v1:.2f} meter pr sekund (m/s)")
    

#1c
def c():
    dist = length_of_one_round()
    t = dist/v1
    print(f"Tiden det tar å sykle 10 runder er {10*t: .2f} sekunder (s)")

while True:
    task = input("Løse a, b, c eller quit?")

    if task=="a":
        a()

    elif task=="b":
        b()

    elif task=="c":
        c()
    else:
        break