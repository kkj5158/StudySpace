from collections import deque

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