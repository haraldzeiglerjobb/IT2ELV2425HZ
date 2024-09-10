maaneder = "JanFebMarAprMaiJunJulAugSepOktNovDes"

while True:
    try: 
        mnd = int(input("Skriv månedsnummeret du ønsker,  1 til 12 eller -1 for quit"))
        
        if mnd ==1:
            print(f"maaneden du ønsker er ",maaneder[0:3])
        elif mnd ==2:
            print(f"maaneden du ønsker er ",maaneder[3:6])
        elif mnd ==3:
            print(f"maaneden du ønsker er ",maaneder[6:9])
        elif mnd ==4:
            print(f"maaneden du ønsker er ",maaneder[9:12])
        elif mnd ==5:
            print(f"maaneden du ønsker er ",maaneder[12:15])
        elif mnd ==6:
            print(f"maaneden du ønsker er ",maaneder[15:18])
        elif mnd ==7:
            print(f"maaneden du ønsker er ",maaneder[18:21])
        elif mnd>7:
            print(f"maaneden du ønsker er ",maaneder[(mnd-1)*3:mnd*3])
        else:
            break

    except:
        print("Feil")

