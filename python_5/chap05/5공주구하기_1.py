from collections import deque
import sys
sys.stdin=open("chap05/5.txt", "r")

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
# 1 2 3 4 5 6 7 8

# 

# cnt = 0 실행  

# 큐의 길이기 1이 될때까지 다음의 과정 반복

# popleft -> append cnt ++ 

#  cnt가 3이면은 popleft만 실행 


