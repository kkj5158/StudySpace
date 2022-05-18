b = [[0] * 3 for _ in range(3)]

#print(b)

b[1][0] = 1
b[1][2] = 1

b[2][0] = 1
b[2][1] = 1

print(b)

for x in b:
    for y in x:
        print(y)