import sys
sys.stdin=open("7.txt", "rt")


n = int(input())

m = [-1]*(n+1) # 0 ~ 200000 # 소수검사 x -1, 소수가 아님 0, 소수임 1 

def checkprime(n):
    if n == 1:
        return 0
    for i in range(2, n):
        r = n % i
        if r == 0 :
            return 0
    
    return 1

cnt = 0

for i in range(1, n+1):
    if m[i] == -1:
        m[i] = checkprime(i)
        if m[i] == 1:
          cnt += 1

    elif m[i] == 1:
        cnt += 1

print(cnt)



        
    
        



