# 음료수 얼려먹기 

# 입력조건의 만족 -> 맵을 어떻게 입력받을 것인가? -> 2차원 배열? 


n, m = map(int, input().split())

map = []

for i in range(n):
    map.append(list(map(int, input()))) # ->2차원 배열의 형성 ? 

# 경로탐색 알고리즘 ? 

#스택과 큐 , 그리고 경로탐색에 필요한 알고리즘 공부하기 
# DFS 와 BFS 에 대한 이해도. 