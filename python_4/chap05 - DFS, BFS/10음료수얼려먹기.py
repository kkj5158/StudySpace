# n,m 입력받기
# 그래프 입력받기 


## 솔루션 보지 말고 반드시 혼자 힘으로 해결하기 


import sys
sys.stdin=open("chap05 - DFS, BFS/10.txt", "rt")

graph = []

count = 0 

n, m = map(int, input().split())

for i in range(n):
    graph.append(list(map(int, input().split())))

def dfs(graph, x, y):
    if x<0 or x>m or y< 0 or y>n:
        return False
    elif graph[x][y] == 1:
         return False
    else:
        graph[x][y] = 1
        dfs(graph, x+1, y)
        dfs(graph, x-1, y)
        dfs(graph, x, y-1)
        dfs(graph, x, y+1)
        count = count + 1
        return True

for x in range(n):
    for y in range(m):
        dfs(graph, x, y)


print(count)
    
# 파이썬 함수 인수 받는법 연습하기 


# 재귀함수는 기능 위주로만 작성한다 . 
# 시작지점 방문한다. -> 0이면 방문처리한다. 1

