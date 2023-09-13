# 입력값 받기 / 맵 입력값 받고서 맵 구현하기 
# 입력값 받기2 / 케릭터 입력값 받기 
# 맵 입력받기 

import sys
sys.stdin=open("chap04 - 구현/4.txt", "rt")

n, m = map(int, input().split())

d = [[0] * m for _ in range(n)]

x, y, direction = map(int, input().split())
d[x][y] = 1

array = []

for i in range(n):
    array.append(list(map(int, input().split())))

# uncomplete 