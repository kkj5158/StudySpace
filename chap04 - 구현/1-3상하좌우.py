n = int(input())
paths = input().split() # 리스트도 따로 선언없이 파이썬의 다음과 같이 간단한 구조로 받을 수 있다. 
x, y = 1, 1

moves = ['L', 'R', 'U', 'D']

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


for path in paths:
    for i in range(len(moves)):
        if path == moves[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx>0 and nx<n+1 and ny>0 and ny<n+1:
        x, y = nx , ny
    
print(x, y)




