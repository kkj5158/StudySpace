import sys
sys.stdin=open("chap06/3.txt", "r")

n = int(input())

chk = [0]*(n+1) 


def dfs(v):
    if v==n+1:
        for idx, val in enumerate(chk):
            if val == 1:
                print(idx , end='')
        print()
    else:
        chk[v] = 1
        dfs(v+1)
        chk[v] = 0
        dfs(v+1)

dfs(1)