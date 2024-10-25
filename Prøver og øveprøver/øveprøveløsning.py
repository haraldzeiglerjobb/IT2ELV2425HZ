"""
Opgpave 1 testes her
"""
def print_t(tab):
    e1 = len(tab)
    e2 = len(tab[0])

    for element in tab:
        print(element)
    print(f"Antall lister i tab: {e1}\nAntall elementer i hver liste: {e2}")
#alternativ 1
#print_t("Alternativ 1")
brett = [
["_","_","_","_","_","_"],
["_","_","_","_","_","_"],
["_","_","_","_","_","_"],
["_","_","_","_","_","_"],
["_","_","_","_","_","_"],
["_","_","_","_","_","_"]
]
print("Alternativ 1")
print_t(brett)

#alternativ 2
brett = [["_"]*7 for i in range(6)]
print("Alternativ 2")
print_t(brett)

#alternativ 3
brett = []
for i in range(6):
    brett.append([])
for j in range(7):
    brett[i].append("_")
print("Alternativ 3")
print_t(brett)

#alternativ 4
brett = []
for i in range(6):
    brett.append(["_","_","_","_","_","_"])
print("Alternativ 4")
print_t(brett)

def fire_like(tab: list):
    for i in range(len(tab)):
        for j in range(len(tab[i])-3):
            sjekkliste = []
            for k in range(4):
                sjekkliste.append(brett[i][j+k])
                if alle_like(sjekkliste) and sjekkliste[0] != "_":
                    vinner = sjekkliste[0]

def alle_like(liste):
    i = 0
    val = liste[0]
    i +=1
    while i < len(liste):
        if liste[i]!=val:
            return False
        i +=1
    return True

sjekkliste = []
sjekkliste.append(["X","X","X","X"])
sjekkliste.append(["X","X","X","O"])	#False	False
sjekkliste.append([1,1,1,1])	    #True	True
sjekkliste.append([2,2,2,"2"])	#usikker	False
sjekkliste.append([1,1,1,True])	#usikker	Truesjekkliste = [5,5,5,True]	#False
sjekkliste.append([0,0,0,False])	#usikker	True

for i in range(len(sjekkliste)):
    print(alle_like(sjekkliste[i]))