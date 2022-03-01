x = int(input())

d = [0] * 1000001

def omin(x):
    if d[x] != 0:
        return d[x]
    else:
        if x == 1:
            d[x] = 0
        else:
            d[x] = omin(x-1) + 1
            if x%2 == 0:
                d[x] = min(d[x], d[x//2]+1)
            if x&3 == 0:
                d[x] = min(d[x], d[x//3]+1)
            if x%5 == 0:
                d[x] = min(d[x], d[x//5]+1)
            return d[x]


print(omin(x))

오류 원인 확인하기 