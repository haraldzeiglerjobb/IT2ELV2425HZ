#program 1
"""
x = int(input("Skriv et tall: "))
y = int(input("Skriv et tall: "))
antallPositive = 0
if x > 0:
antallPositive = antallPositive + 1
if y > 0:
antallPositive = antallPositive + 1
print(antallPositive)
"""

#Program 2
"""
x = int(input("Skriv et tall: "))
y = int(input("Skriv et tall: "))
antallPositive = 0
if x > 0:
antallPositive = antallPositive + 1
elif y > 0:
antallPositive = antallPositive + 1
print(antallPositive)
"""

"""
Forskjellen mellom de to programmene er at
i det ene er det if x>0 og if y>0 og i det siste er det

if x>0 etter fulgt av elif y>0
og det er fundamentalt ulikt, fordi
i det første programmet er det to if-tester

og i det andre er det én if-test etterulgt av en elif-test som 
kun slår til dersom x er mindre enn eller lik 0

I det første programmet er det uavhengige if-tester og det vil 
være korrekt kode for å gjøre det du ønsker å gjøre her 
"""