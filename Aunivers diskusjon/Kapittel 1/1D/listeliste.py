tall = [1,2,3,4]
bokst = ["A","B","C","D"]
navn = ["Anders", "Børre","Charlie","Dina"]

liste = [2, 3.1415, True, [1, "a", 2], "Hallo"]
print(liste[3][0])
liste2 = [tall,bokst, navn]

#ønsker å skrive ut A, Børre, 4
#for å skrive B så må vi gjøre
print(liste2[1][1])
liste = [2, 3.1415, True, [1, "a", 2], "Hallo", liste2]

liste[5][0][2]
#ønsker å skrive ut A, Børre, 4
#A
print(liste2[1][0])
#Børre
print(liste2[2][1])
#4
print(liste2[0][3])

#ønsker å skrive ut C, Charlie, 3.1415 fra liste
#C
print(liste[-1][1][2])
#Charlie
print(liste[5][2][2])
#3.1415
print(liste[1])
