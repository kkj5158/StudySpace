from collections import deque
import sys

sys.stdin=open("chap05/6.txt", "r")


def getmax(a):
    max = 0

    for i in range(len(a)):
        if a[i][1] > max:
            max = a[i][1]
    
    return max
            

n, m = map(int, input().split())

Q=[(pos, val) for pos, val in enumerate(list(map(int, input().split())))]

Q=deque(Q) # [(0, 60), (1, 50) , (2, 70) , (3, 80) , (4, 90)]

cnt = 0

while True:
    cur = Q.popleft()
    if cur[1]  < getmax(Q):
        Q.append(cur)
    else:
        cnt = cnt+1
        if cur[0] == m:
            break

print(cnt)



# 5 2 
# 60 50 70 80 90

# 50 70 80 90 60

# 70 50 80 90 60  

# 반복문은 해당 번호가 나올때까지 반복한다 . 
# max값보다 작으면 push, max값과 동일하거나 크면 pop하고 카운트를 1올린다. 


# 60 60 90 60 60 60




