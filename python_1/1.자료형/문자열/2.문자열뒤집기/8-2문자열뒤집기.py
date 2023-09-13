import sys
sys.stdin=open("chap02/8.txt", "rt")

n = int(input())

a = list(map(int, input().split()))


"""
문자열 뒤집기를 구현하는 3가지 알고리즘 

https://blockdmask.tistory.com/581
"""

# 2 . 리스트의 reverse 기능 활용하기 

def reverse(x):
    x = list(str(x))
    x.reverse()

    x = ''.join(x)

    
    return int(x)
  




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
