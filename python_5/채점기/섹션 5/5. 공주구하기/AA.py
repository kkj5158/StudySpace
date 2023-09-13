from collections import deque

num , cnt = map(int, input().split())

que = deque()

for i in range(1, num+1):
    que.append(i)
    

i=1

while 1:
    if(len(que)==1):
        break

    if i == cnt:
        que.popleft()
        i=0
    else:
        que.append(que.popleft())

    i  = i+1


result = que.popleft()

print(result)