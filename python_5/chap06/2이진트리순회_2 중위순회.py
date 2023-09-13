import sys

sys.stdin=open("chap06/2.txt", "r")

# 전위순회 

def DFS(v):
    if v>7:
        return
    else:
        DFS(v*2)
        print(v, end='')
        DFS(v*2+1)


# dfs는 재귀를 통해서 구현한다. 

DFS(1) 