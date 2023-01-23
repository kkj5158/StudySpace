from collections import deque
import sys

sys.stdin=open("chap05/8.txt", "r")

n = int(input())

note = deque()

poem = deque()

# 큐의 길이만큼 반복한다. 

# 팝한다. 첫번째 단어와 비교한다. 틀리면 다시 푸쉬한다. 
# 맞으면 푸쉬하지 않는다. 
# 마지막으로 남은 단어를 출력한다. 


for _ in range(n):
    note.append(input())

for _ in range(n-1):
    poem.append(input())

for i in range(n-1):
    for j in range(len(note)):
        a = note.popleft()

        if poem[i] != a:
            note.append(a)

print(note.popleft())