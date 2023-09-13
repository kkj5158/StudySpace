import sys

sys.stdin=open("chap06/6.txt", "r")

n, m = map(int, input().split())

arr = [0 for _ in range(m)]

cnt = 0

def DFS(v):
    global cnt 

    if v==m:
        print(*arr, sep="")
        cnt = cnt + 1
    else:
        for i in range(1, n+1):
            arr[v] = i
            DFS(v+1)
    

DFS(0)
print(cnt)