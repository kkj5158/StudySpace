# 피보나치 수열을 풀이하는 다이나믹 프로그래밍 알고리즘 보지 않고 완벽 구상하기 

x = int(input())

p = [0]*10000

def fibo(x):
    if(p[x] != 0):
        return p[x]
    else:
        if x==1 or x==2:
            p[x] = 1
            return 1
        else:
            p[x] = fibo(x-1) + fibo(x-2)
            return p[x]


print(fibo(x))

