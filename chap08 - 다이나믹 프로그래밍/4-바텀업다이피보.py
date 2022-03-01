x = int(input())

p = [0]*100000

def pibo(x):
    for i in range(1, x+1):
        if(p[i] != 0):
            continue
        else:
            if(i==1 or i==2):
                p[i] = 1
            else:
                p[i] = p[i-1] + p[i-2]

    return p[x]

print(pibo(x))