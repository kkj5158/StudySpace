import sys
sys.stdin=open("chap04/8.txt", "rt")

cnt = 0

def check(lis, m):
    min = lis[0]

    sum = 0

    for _ in range(lis[1:]):
        i = -1
        sum = min + lis[i]
        i += -1 
        
        if sum <= m:
            cnt += 1
            break
        

n, m = map(int, input().split())

ar = map(int, input().split())

ar.sort()



# 50 60 70 90 100

# max = 사람마다 하나의 보트가 필요 n개
# min = 모든 보트에 2명이 탑승 
# 최소 보트의 갯수는 다음과 같이 구할수 있음 -> 최대 보트의 갯수 (max) - 2명이 보트에 탑승할경우 보트 1개 빼기 

cnt = n

