"""
Dette programmet skal lære deg å lage klasser fra skrætsj
"""
import math
class WhateverClass():
    """
    Dokumentasjonsstreng for klassen...
    Denne klassen WhateverClass skal være en generisk
    pedagogisk klasse for å lære om klasser
    """

    #dette kalles en klassevariabel
    klassevariabel_1 = math.pi

    def __init__(self, parameter1: int = 6, 
                 parameter2: str = "Hest er best",
                 parameter3: list = []):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.parameter3 = parameter3
        #Note to self (pun intended): bruk kortere og mer beskrivende
        #variabelnavn enn de jeg har brukt... :)

        #Og en ting til:
        #Parametrene som tilegnes objekter kalles attributter!
        #Attributter altså
        #Husk det

    def objektmetode1(self):
        """
        Dokumentasjonsstreng for metoden
        Og ja... funksjoner for objekter kalles heretter
        METODER (ikke i kapitéler (store bokstaver))
        Metoder altså
        Metoder
        Husk det.... :) 
        """

        print("Something")  #Hvis du vil printe noe
        a = 8   #lag en variabel
        #Du kan gjøre alt du ville gjort i en funksjon her
        #men... husk at self er referansen til objektet
        self.attributt1 = self.parameter1
        #innfører en ny variabel som heter attributt1
        return True #Kanskje du vil returnere noe? Det kan du jo gjøre!
    
    def print(self):
        """
        Her kan du erstatte print-metoden i Python til å printe informasjon
        om objektet, som er tilpasset det spesifikke objektet du har med å gjøre
        """

        s0 = "Overskrift: Objektets egenskaper er:\n"
        s1 = f"Egenskap 1: parameter1 som burde kalles attributt 1 = {self.parameter1}\n"
        s2 = f"Egenskap 2: parameter2 som burde kalles attributt 2 = {self.parameter2}\n"
        s3 = f"Egenskap 3: parameter3 som burde kalles attributt 3 = {self.parameter3}\n"

        print(s0,s1,s2,s3)

def main():
    #vi kaller metoden uten å bruke self!
    objekt1 = WhateverClass()
    objekt1.objektmetode1()
    objekt1.print()

#Her kommer en standardmetode for å kjøre programmet med en test-loop i
#tilfelle det er hovedprogrammet 
#men det kan hende at du importerer det til bruk i et annet program
#uansett: __main__ er en privat attributt, som indikerer om det er 
#hovedprogrammet eller ikke
if __name__=="__main__":
    main()
#main()