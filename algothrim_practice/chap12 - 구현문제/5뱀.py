n = int(input())
k = int(input())

# map 구현하기 
map = [[0 for col in range(n+2)] for row in range(n+2)]

moves = []

# 맵 정보 ( 사과 있는 곳은 1로 표시 )

for _ in range(k):
    a, b = map(int, input().split())
    map[a][b] = 1



# 움직이는 횟수 입력받기 

l = int(input())

# move 입력받기 
for i in range(l):
    x , c = input().split()
    moves.append((int(x), c))


# 방향 설정하기 (동, 남, 서 , 북  ) # -> x 좌표 
dx = [1, 0, -1, 0]  
dy = [0, 1, 0, -1]

def turn(direction, c):
    if c == "L":
        direction = (direction - 1) % 4
    else : 
        direction = (direction + 1) % 4
    return direction

def simulate():
    x, y = 1, 1 # 뱀의 머리 위치
    data[x][y] = 2 # 뱀이 존재하는 위치는 2로 표시
    direction = 0 # 처음에는 동쪽을 보고 있음
    time = 0 # 시작한 뒤에 지난 '초' 시간
    index = 0 # 다음에 회전할 정보
    q = [(x, y)] # 뱀이 차지하고 있는 위치 정보(꼬리가 앞쪽)

    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        # 맵 범위 안에 있고, 뱀의 몸통이 없는 위치라면
        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2:
            # 사과가 없다면 이동 후에 꼬리 제거
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                data[px][py] = 0
            # 사과가 있다면 이동 후에 꼬리 그대로 두기
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx, ny))
        # 벽이나 뱀의 몸통과 부딪혔다면
        else:
            time += 1
            break
        x, y = nx, ny # 다음 위치로 머리를 이동
        time += 1
        if index < l and time == info[index][0]: # 회전할 시간인 경우 회전
            direction = turn(direction, info[index][1])
            index += 1
    return time

print(simulate())