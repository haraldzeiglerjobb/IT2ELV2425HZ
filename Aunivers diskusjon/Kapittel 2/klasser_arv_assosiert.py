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


class assosiert:
    """docstring for the class assosiert"""
    def __init__(self, param1):
        self.param1 = param1
    def method1(self):
        pass

class composition:
    """docstring for the class composition"""
    def __init__(self, param1):
        self.param1 = param1
    def method1(self):
        pass

class Appelsin(Frukt):
    """docstring for the class Appelsin"""
    
    farge = "oransje"
    smak = "søt og god"
    
    def __init__(self, produsent, assos: assosiert, farge: str = "oransje", land = "Spania", vekt: int =100):
        #Konstruktør
        super().__init__(produsent, farge)
        self.vekt = vekt
        self.land = land
        self.assos = assos
        self.compos = []

    def objektmetode(self, compos: composition):
        #mal for objektmetoder... husk "self"
        self.compos.append(compos)

    def print_me(self):
        super().print_me()
        print(f"Smaken er {Appelsin.smak}")
        print(f"Frukten er fra {self.land}")
        print(f"Vekten er {self.vekt}")
        
    def print_class():
        super().print_class()

harald = Appelsin("Bama")
print(harald.produsent)
print(Appelsin.farge)
harald.print_me()