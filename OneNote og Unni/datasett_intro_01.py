"""
	1. Lag et program som spør brukeren om å oppgi et tall, om og om igjen, helt til brukeren oppgir q istedenfor et tall. Samle alle verdiene i en liste. Lag to løsninger, en variant uten, og en variant med standardfunksjonenen sum() og len() )
		a. Da skal alle tallene, og summen av alle tallene som ble oppgitt skrives ut.
		b. ... og gjennomsnittet av tallene

"""

def sum_of_list(xl: list = []):
    partial_sum = 0
    for x in xl:
        partial_sum += x
    return partial_sum

def number_of_elements(xl: list = []):
    #useless function, use len(xl) instead
    i = 0
    for element in xl:
        i +=1
    return i

def average(xl: list = []):
    return sum_of_list(xl)/number_of_elements(xl)

my_list = []
while True:
    a = input("Skriv inn et tall eller q for å avslutte")

    try: 
        x = int(a)
    
    except:
        if a=="q":
            print("quit input....")
            break
    else:
        my_list.append(x)
        print("Here we go again!")

print("Ute av løkka, tid for tallbehandling")


print(my_list)
print(f"Summen av alle tall i listen er {sum_of_list(my_list)}")
print(f"Average value is {average(my_list):.2f}")

