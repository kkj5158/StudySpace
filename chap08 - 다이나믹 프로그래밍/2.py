d = [0]*100

def fibo(x):
    if x==1 or x==2:
        return 1
    if d[x] != 0 :
        return d[x]
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))

# 피보나치 수열을 기반으로 하는 다이나믹 프로그래밍 알고리즘 보지 않고 완벽하게 구상하기 #