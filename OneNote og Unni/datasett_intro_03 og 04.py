"""	3. Programmer en liste med 50 tilfeldige heltall [1,10]. 
		a. Tell opp antall av hvert siffer uten å bruke metoden .count(), lag en utskrift av hvor mange det er av hvert siffer 1 - 10 i tabellform.
Utvid programmet med å bestemme typetall (den verdien det er flest av). Kan være mer enn ett tall
"""
import random as rd

#checksum
def check_sum(xl):
    cs = 0
    for x in xl:
        cs +=x
    return cs

my_list = [rd.randint(1,10) for x in range(50)]
print(my_list)

#Velger en tabellstruktur som er slik: indeks n-1 inneholder antall elementer med verdi n

counter = [0 for _ in range(10)]

#algorithm: for each occurrence of element in my_list, increase corresponding counter-value
for x in my_list:
    counter[x-1] +=1
print("Antall av hver type:",counter)

#testing
if check_sum(counter) == 50:
    print("Yess! Summen er 50")
else:
    print("Something wrong")

#b med metoden count
counter2 = [0 for _ in range(10)]

for i in range(10):
    counter2[i]=my_list.count(i+1)
print("Antall av hver type med count():",counter2)