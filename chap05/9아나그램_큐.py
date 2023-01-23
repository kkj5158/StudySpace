from collections import deque
import sys

sys.stdin=open("chap05/9.txt", "r")

w1 = deque(str(input()))
w2 = deque(str(input()))


# 회전시키자. 같은게 나올때까지

# for문 첫번째 원소를 기준으로 원소의 갯수만큼 다시 for 문

# 첫번째 원소와 같은 놈이 나올때까지 회전시킨다 (push pop)

# 원소와 같은 놈이 나오면은 그놈은 pop으로 완전히 빼낸다. 

# 만약 모든 원소의 갯수만큼 회전시켜도 같은놈이 안나오면 no를 출력한다.

# 모든 for문을 완벽히 돌고나서. w2의 길이가 0일경우 yes를 출력한다

for i in w1:
    for _ in range(len(w2)):
        isin = 0
        cur = w2.popleft()
        
        if i != cur :
            w2.append(cur)
        else:
            isin = 1
            break
    if isin == 0:
        print("NO")
        break

if len(w2) == 0:
    print("YES")
            