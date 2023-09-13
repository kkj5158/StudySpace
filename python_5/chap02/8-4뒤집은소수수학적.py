import sys
sys.stdin=open("chap02/8.txt", "rt")


n = int(input())

a = list(map(int, input().split()))

# 앞의 수부터 뒤로 옮겨간다. 

def reverse(x):
    max = 10000
    min = 1

    newx = 0 
    
    while  x > 0 :
        q = x // max
        if (q== 0):
            max = max//10
        else:
            newx = newx + q*min
            x = x - q*max
            min = min*10
            max = max//10

    return newx         



def isPrime(x):
    if x == 1 :
        return 0
    elif x == 2:
        return 1
    else:
        for i in range(2, x):
            if x%i == 0:
                return False # 소수가 아니다 .
        else:
            return True # 소수이다. 

    

for num in a :
    n = reverse(num)
    if(isPrime(n)):
        print(n, end=' ')

    