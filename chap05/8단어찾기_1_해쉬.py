from collections import deque
import sys

sys.stdin=open("chap05/8.txt", "r")

n = int(input())

note = dict()

poem = []


for _ in range(n):
    note[input()] = 0

for _ in range(n-1):
    poem.append(input())


for a in poem:
    note[a] = 1


for a in note:
    if note[a] == 0:
        print(a)
        break


# 딕셔너리(해쉬)를 사용한다. 

# 단어들을 key로 사용한다. value = 0 으로 모두 초기화한다. 

# 해당 단어들이 존재하면 value를 1로 업데이트 한다. 

# 모두 체크한 이후에 value가 0인 단어가 존재한다면 그 단어가 시에쓰지 않은 한개의 단어이다. 

