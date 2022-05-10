n = int(input())

a = []

for i in range(n):
    b = list(map(int, input().split()))
    a.append(b)


def countsame(x):
    if x.count(x[0]) == 3:
        return x[0], 3
    elif x.count(x[0]==2):
        return x[0], 2
    elif x.count(x[1]==2):
        return x[1], 2
    elif x.count(x[2]==2):
        return x[2], 2
    else:
        x.sort()
        return x[2], 1



def countprice(g, n):
    if n == 3:
        return 10000 + g*1000
    elif n==2:
        return 1000 + g*100
    else:
        return g*100



max = 0

for i in range(n):
    g, n = countsame(a[i])
    price = countprice(g, n)

    if(price>max):
        max = price


print(max)