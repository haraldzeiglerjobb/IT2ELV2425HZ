while True:
    try:
        points=int(input("hvor mange oppgaver fikk du riktig? "))
    except:
        print("du må oppgi ett tall")
    else:
        break

if(points <=100) and (points >=0):
    if points < 21:
        print("du fikk karakteren 1")
    elif points < 41:
        print("du fikk karakteren 2")
    elif points < 61:
        print("du fikk karakteren 3")
    elif points < 81:
        print("du fikk karakteren 4")
    elif points < 91:
        print("du fikk karakteren 5")
    else:
        print("du fikk karakteren 6")