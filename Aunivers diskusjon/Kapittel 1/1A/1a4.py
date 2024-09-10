fjella = ["Galdhøpiggen","Glittertind", 
         "Store Skagastølstind", "Store Styggedalstind", "Skarstinden"]

hoyder = [2469, 2472, 2405, 2387, 2374]


for i in range(len(fjella)):
    print(fjella[i][0:3],"...",fjella[i][-3:]," h: ",hoyder[i])