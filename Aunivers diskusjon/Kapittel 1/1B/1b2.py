while True:

    poeng = int(input("Skriv en heltallig poengsum mellom 0 og 100"))

    if poeng <0 or poeng>100:
        print("Utafor skalaen")
    elif poeng>=0 and poeng <21:
        print("Karakter 1")
    elif poeng >=21:
        if poeng <=40:
            print("Karakter 2")
        else:
            if poeng <=60:
                print("Karakter 3")
            elif poeng <=80:
                print("Karakter 4")

            elif poeng <=90:
                print("Karakter 5")
            else:
                print("Karakter 6")