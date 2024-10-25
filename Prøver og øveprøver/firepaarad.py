import øveprøveløsning as øp
def print_t(tab):
    e1 = len(tab)
    e2 = len(tab[0])

    for element in tab:
        print(element)
    print(f"Antall lister i tab: {e1}\nAntall elementer i hver liste: {e2}")

def print_tr(tab):
    e1 = len(tab)
    e2 = len(tab[0])
    i = 0
    while i < len(tab[0]):
        j=0
        while j < len(tab):

           print("|",end="")
           print(tab[j][i],end="")
           j +=1
        print("|")
        i +=1
    print(f"Antall lister i tab: {e1}\nAntall elementer i hver liste: {e2}")

brett = [["_"]*7 for x in range(6)]
brett_t = [["_"]*6 for x in range(7)]
print(brett)
print(brett_t)
print_t(brett)
print_tr(brett_t)

def legg_i_kolonne(tab, nummer, symbol):
    plass = False
    for i in range(len(tab), -1,-1):
        if tab[i][nummer]=="_":
            plass = True
            tab[i][nummer]=symbol
            break
    if not plass:
        print()
        print(f"Kolonne {nummer} er full, velg en annen")
        print()

kol = int(input("Velg en kolonne mellom 1 og 7\n"))-1
#legg_i_kolonne(brett, kol, "X")
brett[5][kol]="X"
print_t(brett)
brett_t[kol][5]="X"
print_tr(brett_t)

for i in range()