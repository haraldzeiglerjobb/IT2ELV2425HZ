# Lister blir fort uoversiktlige - hva betyr egentlig 2007 og 2003 her?
person1 = ["Unni",54,175,2007,2003]

#person1[3]

# Ordbøker er bedre variabler, for de forklarer hva hver verdi betyr
person2 = {
  "navn" : "Unni",
  "alder" : 54,
  "hoyde" : 175,
  "ansatt" : 2007,
  "klatret_siden" : 2003
}


# Med flere variabler av typen ordbøker så kan det være fort gjort å 
# få noen skrivefeil, f.eks her har katt1 nøkkelordet "type", mens
# katt2 har nøkkelordet "rase"

katt1 = {
  "navn" : "Silkesvarten",
  "type" : "Norsk skogkatt",
  "farge" : "Svart"
}

#katt1["alder"] = 5

katt2 = {
  "navn" : "Tigergutt",
  "rase" : "Norsk skogkatt",
  "farge" : "Stripete grå-svart"
}

hund1 = {
  "navn" : "Kaisa",
  "rase" : "Labrador retriever",
  "farge" : "Svart"
}

# For enklere behandling med løkker, så tar vi gjerne ordbøker inn i en liste
mine_dyr = [katt1, katt2, hund1]

# Funksjoner kalles også prosedyrer, derav prosedyreorientert programmering

def snakk_katt(dyr):
  print(dyr["navn"],'sier "Mjau"')

def snakk_hund(dyr):
  print(dyr["navn"],'sier "Voff"')

def dyr_info(dyr):
  print(dyr["navn"],"er en",dyr["farge"].lower(),dyr["rase"].lower())

# Noen funksjoner kan brukes for alle dyrene:

for dyr in mine_dyr:
  dyr_info(dyr)

# Noen funksjoner virker bare for enkelte dyr, kan ikke bruke løkke her:
snakk_katt(mine_dyr[0])
snakk_hund(mine_dyr[2])

# Klasser har navn som starter med stor forbokstav
# Det betyr at variabler og funksjoner skal IKKE starte med stor forbokstav
# Nye ord: parametrene eller variablene kalles nå egenskaper... self.egenskap
#          funksjonene kalles nå metoder... self.metode() 
class Dyr:

  antalldyr_i_verden = 10

  def __init__(self,navn,rase,farge,hale="Lang"): # parametre med defaultverdi skrives sist
    self.navn = navn
    self.rase = rase
    self.farge = farge
    self.hale = hale
    self.alder = 0       # kan ha egenskaper som ikke angis som parameter

  def dyr_info(self):    # metoder har alltid parameteren self
    print(self.navn,"er en",self.farge.lower(),self.rase.lower())

  def aldring(self,antall):   # metoder kan ha flere parametre
    self.alder += antall
    print(self.navn,"er nå",self.alder,"år")


# Et OBJEKT er en variabel som baserer seg på en klasse:
 
katt1 = Dyr("Pus","Tibetansk nakenkatt","Lysebrun","Kort")

print(katt1.navn)     # refererer til en egenskap

katt1.dyr_info()      # refererer til en metode 

katt1.aldring(4)      # legg merke til at metoden aldring bare har ett argument,
                      # selv om den er definert med to. Vi oppgir ikke verdi for self.
                      
mine_dyr = [
  Dyr("Silkesvarten","Norsk skogkatt","Svart"),
  Dyr("Tigergutt","Norsk skogkatt","Stripete grå-svart"),
  Dyr("Kaisa","Labrador retriever","Svart")
]

for dyr in mine_dyr:
  dyr.dyr_info()
  dyr.aldring(3)

mine_dyr[2].aldring(5)