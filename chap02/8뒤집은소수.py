import sys
sys.stdin=open("8.txt", "rt")

n = int(input())

a = list(map(int, input().split()))

def reverse(x):
    a = str(x)
    
    a = a[::-1]

    return int(a)




def isPrime(x):
    if x == 1 :
        return 0
    elif x == 2:
        return 1
    else:
        for i in range(2, x):
            if x%i == 0:
                return False # 소수가 아니다 .
    
    return True # 소수이다. 

for num in a :
    n = reverse(num)
    if(isPrime(n)):
        print(n, end=' ')
