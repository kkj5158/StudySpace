# 지도의 크기하고 이동 계획 입력받기 
# 이동하면서 이동이 가능할시에 이동, 이동이 불가능하면 그 자리에 그대로 머물기 

n = int(input())
x, y = 1, 1
paths = input().split()



moves = ['L', 'R', 'U', 'D']

dy = [-1, 1, 0 , 0]

dx = [0, 0 , -1, 1]


for path in paths:
    for i in range(len(moves)):
        if(moves[i] == path):
            nx = x + dx[i]
            ny = y + dy[i]
    if(nx>0 and nx < n+1 and ny > 0 and ny < n+1):
            x , y = nx, ny

print(x,  y)


