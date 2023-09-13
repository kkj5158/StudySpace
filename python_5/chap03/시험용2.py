def changesequence(list,a,b):
    nlist = list[b:a-1:-1]
    print(nlist)
    j = 0
    for i in range(a, b+1):
        list[i]=nlist[j]
        j=j+1

    return list


l = [0]

for i in range(1,21):
    l.append(i)

changesequence(l, 4, 8)

print(l)