
from collections import deque
import sys
sys.stdin=open("chap04/8.txt", "rt")

n, m = map(int, input().split())

ar = list(map(int, input().split()))

ar.sort()

ar = deque(ar)

cnt = 0 

head = 0
tail = n-1

while ar:
    if len(ar) == 1:
        cnt+=1
        break
    if ar[0] + ar[-1] > m:
        ar.pop()
        cnt+=1
    else:
        ar.popleft()
        ar.pop()
        cnt+=1

print(cnt)
        
    
        




# 50 60 70 90 100

# max = 사람마다 하나의 보트가 필요 n개
# min = 모든 보트에 2명이 탑승 
# 최소 보트의 갯수는 다음과 같이 구할수 있음 -> 최대 보트의 갯수 (max) - 2명이 보트에 탑승할경우 보트 1개 빼기 




