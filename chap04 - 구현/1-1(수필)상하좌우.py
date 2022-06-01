# type error 체크하기 
import sys
sys.stdin=open("chap04 - 구현/1.txt", "rt")


n = map(int, input().split())
x, y = 1, 1

plan = input().split()

move = ['L' , 'R', 'U', 'D']

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in plan:

    for i in range(len(move)):
        if plan[i] == move[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x,y)


# uncomplete# 