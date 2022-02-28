x = int(input())

p = [0]*100000

def pibo(x):
    for i in range(1, x+1):
        if(p[i] != 0):
            continue
        else:
            if(x==1 or x==2):
                p[i] = 1
            else:
                p[i] = p[i-1] + p[i-2]

    return p[x]

print(pibo(x))

왜 잘못된 값이 나오는지 고찰해보기 . 

코드 조금 더 간결한 값을 변환해보기 . 