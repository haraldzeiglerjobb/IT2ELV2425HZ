def fakultet(x):
    if x==1:
        return 1
    else:
        return x*fakultet(x-1)
    
"""for i in range(1,6):
    print(f"Faultet med {i} er {fakultet(i)}")
"""
#løsningsforslag
def fakultet_ny(x: int = 1)  -> int:
    """
    Denne funksjonen fikser opp i fakutlet med en fiks a vinput
    """
    if x==0 or x==1:
        return 1
    else:
        #hvis alt annet skjer, returner funksjonen selv ganget med argumentet
        return x*fakultet_ny(x-1)
    
while True:
    try:
        x = int(input("Skriv inn et heltall"))
    except ValueError:
        print("Du skrev ikke innet heltall")
    else:
        print(fakultet_ny(x))
        break

    
fakultet_ny()