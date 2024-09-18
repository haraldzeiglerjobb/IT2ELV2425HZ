def f(x):
    print("hei")

def g(x):
    return 2*x+1

f(1)

print(g(1))

#ekse
def h(x,y,z,æ,ø,å): #parametere inni parentesen
    return 1 #something

h(1,2,3,4,5,6) #argumentene er de du faktisk sender inn
#x = 1, y = 2, z = 3, æ = 4, ø = 5, å = 6
h(x =9, y = 8, z = 5, ø = 1, å = 0, æ = 5)

def k(x = 0,y = 5,z= 9):
    print("hei:::k")
    print(x,y,z)

k()

#teste: hva skjer hvis vi skriver noen ,men ikke alle, og 
k(x=9)
k(1)