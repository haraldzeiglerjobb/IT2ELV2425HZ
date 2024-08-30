maaneder = "JanFebMarAprMaiJunJulAugSepOktNovDes"
måned=int(input("skriv inn et månedsnummer fra 1-12 "))
if 1 <= måned <= 12 :
    #print("Månedforkortelsen er ",maaneder[(måned-1)*3:måned*3])
    print(f"Månedforkortelsen er {maaneder[(måned-1)*3:måned*3]}")
else:
    print("Skriv et tall fra 1-12")