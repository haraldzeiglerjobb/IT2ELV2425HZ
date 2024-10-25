"""
Objekter:
Ting
med kjennetegn

Oppgave: Lag din egen klasse [velg navn] og bruk konstruktør
"""
class Frukt:

    #klassevariabler
    farge = "oransje"
    smak = "god"

    def __init__(frukt, farge: str = "", produsent = ""):

        frukt.farge = farge
        frukt.produsent = produsent


class Appelsin(Frukt):
    #klassevariabler
    #vekt = "høy"
    
    def __init__(sjøl, produsent, land = "Spania", vekt: int =100):
        #Konstruktør
        super().__init__(produsent)

harald = Appelsin("Bama")
print(harald.produsent)
print(Appelsin.farge)