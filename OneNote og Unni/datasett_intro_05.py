"""	
	5. Programmer en liste med lottotallene (7 tilfeldige heltall [1,34], ingen tall skal gjentas). Lag programmet på minst to forskjellige måter.
"""
import random as rd
top = 34
bottom = 1
number_of = 7

#strategi 1: Trekk fra en liste med alle tall 1 til 34, pop de som brukes
lottery_numbers = [x for x in range(1,35)]
print(lottery_numbers)

my_numbers = []
for x in range(number_of):
    t = rd.choice(lottery_numbers)
    my_numbers.append(t)
    lottery_numbers.remove(t)

print(sorted(my_numbers))
print(lottery_numbers)

#Metode 2: Ved å lage en liste med valgte tall
my_numbers = []
i = 0
while i < number_of:
    choice = rd.randint(bottom, top)
    if choice not in my_numbers:
        my_numbers.append(choice)
        i +=1
print(sorted(my_numbers))
