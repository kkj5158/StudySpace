from collections import deque
import sys

sys.stdin=open("chap05/9.txt", "r")

# 단어 하나를 key 갯수를 value라고 하는 dic 만들기 

# 입력에 따라서 dic 업데이트

# 두개의 딕셔너리가 동일한지 확인. 확인후 동일하면 yes, 아니면 no 

w1 = input()
w2 = input()

dicw1 = dict()
dicw2 = dict()

for s in w1:
    if s in dicw1:
        dicw1[s] += 1
    else:
        dicw1[s] = 0

for s in w2:
    if s in dicw2:
        dicw2[s] += 1
    else:
        dicw2[s] = 0

if dicw1 == dicw2:
    print("YES")
else:
    print("NO")