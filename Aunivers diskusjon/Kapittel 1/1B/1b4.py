a = input("Skriv inn et tall (tall1)")
b = input("Skriv inn et tall (tall2)")
c = input("Skriv inn et tall (tall3)")

#4a
#Programmet skal sjekke om alle tallene er like

if a==b:
    if b==c:
        print("De er like!")
    else:
        print("De er ikke like")

#4b
#Les inn et heltall sjekk om det er partall eller oddetall

a = int(input("Skriv inn et heltall!"))
if a%2==0:
    print(f"a ({a} er et partall")'
else:
    print(f"a ({a}) er et oddetall")