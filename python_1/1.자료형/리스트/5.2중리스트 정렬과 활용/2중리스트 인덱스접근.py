members = [[172, 67], [183, 65], [180, 70], [170, 72], [181, 60]]


for m in members:
    print(m[0])

for m in members:
    print(m[1])


h = 10

for m in members:
    if h < m[0]:
        print("end")