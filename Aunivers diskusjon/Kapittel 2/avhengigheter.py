"""
Viser avhengigheter

Bygg inn
' arv
- asossiasjon
avhengighet
"""

class superklasse:

    def __init__(self):
        pass

class avhengig_klasse:

    def __init__(self):
        pass

class underklasse(superklasse):

    def __init__(self, assosiert):
        self.assosiert = assosiert

    def metode(self, avhengig: avhengig_klasse = None):
        print("bruker en avhengig klasse")

class assosiert_klasse:
    def __init__(self):
        pass