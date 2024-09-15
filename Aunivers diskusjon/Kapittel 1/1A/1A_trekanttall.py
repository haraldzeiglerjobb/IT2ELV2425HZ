def trekanttall(x):
    return x*(x+1)/2

counter = 0

for i in range(10):
    counter = counter + trekanttall(i+1)

print(counter)
