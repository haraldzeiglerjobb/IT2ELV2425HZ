"""
Objekter:
Ting
med kjennetegn

Oppgave: Lag din egen klasse [velg navn] og bruk konstruktør
"""
class Frukt:

    #klassevariabler
    farge = ""
    smak = ""

    def __init__(frukt, farge: str = "", produsent = ""):

        frukt.farge = farge
        frukt.produsent = produsent

    def print_me(self):
        print(f"Frukten heter {self.__class__}")
        print(f"Frukten smaker {self.smak}")
        print(f"Frukten er produsert av {self.produsent}")
        
    def print_class():
        print(Frukt.farge)
        pass



class Appelsin(Frukt):
    
    farge = "oransje"
    smak = "søt og god"
    
    def __init__(sjøl, produsent, farge: str = "oransje", land = "Spania", vekt: int =100):
        #Konstruktør
        super().__init__(produsent, farge)
        sjøl.vekt = vekt
        sjøl.land = land

    def objektmetode(sjøl):
        #mal for objektmetoder... husk "sjøl"
        pass

    def print_me(sjøl):
        super().print_me()
        print(f"Smaken er {Appelsin.smak}")
        print(f"Frukten er fra {sjøl.land}")
        print(f"Vekten er {sjøl.vekt}")
    def print_class():
        super().print_class()

harald = Appelsin("Bama")
print(harald.produsent)
print(Appelsin.farge)
harald.print_me()