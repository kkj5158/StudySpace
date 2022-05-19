import sys
sys.stdin=open("chap02/8.txt", "rt")


n = int(input())

a = list(map(int, input().split()))

# 뒤의 수부터 앞으로 옮겨간다. 


def reverse(x):
    q = 10 
    newx = 0
     

    while x > 0 :
      r = x % q
      x = x // q
      newx = newx*10 + r

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

    