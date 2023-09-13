from collections import deque
import heapq as hq
import sys

sys.stdin=open("chap05/10.txt", "r")

# 부모노드의 값이 항상 자식보다 작아야 한다. 

# 입력후 부모와의 비교 . 

# 부모보다 자기가 작으면 부모와 스왑이 일어난다. 아니면은 그냥 멈추기 

# 최소힙의 구현 입력은 항상 레벨순으로 구현된다. 

# pop 이후에는 두개의 자식을 비교해서 적은 놈을 올린다. 이를 레벨별로 계속 반복한다. 

# 어떻게 구현할 것인가 . 

 
a = []

while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        if len(a) == 0:
            print(-1)
        else:
            print(hq.heappop(a))
    else:
        hq.heappush(a, n)