import sys
sys.stdin=open("7.txt", "rt")


n = int(input())

m = [-1]*(n+1) # 주어진 n+1 까지의 소수인지 아닌지 값을 결정하는 배열 # -1 체크되지 않음, 1은 소수임 0은 소수아님 

def checkprime(n):
    if n == 1:
        return 0
    for i in range(2, n):
        r = n % i
        if r == 0 :
            return 0
    
    return 1

def checknotprime(arr,p):
    while p < len(arr):
        i=2
        arr[p] = 0
        p = p*i
        i+=1

cnt = 0

for i in range(1, n+1):
    if m[i] == -1:
        m[i] = checkprime(i)
        if m[i] == 1:
          cnt += 1
          checknotprime(m, i)

    elif m[i] == 1:
        cnt += 1

print(cnt)


