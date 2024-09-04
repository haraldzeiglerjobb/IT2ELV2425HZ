tall = [2, 4, 6, 8, 10]
j = tall[3]

for i in tall:
    if i >j:
        j = i
print(j)

j = tall[3]
for k in range(len(tall)):
    if tall[k] <j:
        j = tall[k]
print(j)

m = max(tall)
print(m)