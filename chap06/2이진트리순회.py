def DFS(v):
    if v>7:
        return
    else:
        DFS(v*2)
        DFS(v*2+1)
        print(v, end=' ')


DFS(1)