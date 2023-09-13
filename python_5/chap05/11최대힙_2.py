import heapq as hq
import sys

sys.stdin=open("chap05/11.txt", "r")
a=[]

# -를 이용해서 최소힙을 거꾸로 사용하기 


while True:
    n=int(input())
    if n==-1:
        break
    if n==0:
        if len(a)==0:
            print(-1)
        else:
            print(-hq.heappop(a))
    else:
        hq.heappush(a, -n)
