import sys

sys.stdin=open("chap06/7.txt", "r")

n = int(input())

lis = list(map(int, input().split()))

m = int(input())

mincnt = 2e9

def dfs(v , total, cnt):
    global mincnt

    if total > m:
        return
    if cnt > mincnt:
        return 

    if total == m:
        mincnt = cnt
    else:
        for c in lis:
            dfs(v+1, total+c, cnt+1)
             
dfs(0, 0 , 0)

print(mincnt)


