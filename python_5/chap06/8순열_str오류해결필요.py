import sys

sys.stdin=open("chap06/8.txt", "r")

n, m = map(int, input().split())

# arr = [0 for _ in range(m)]


def dfs(v, arr):
    global n 

    if v==m:
        print(arr)
    else:
        numlis = [j for j in range(1, n+1)]

        if len(arr)>0:
            for n in arr:
                numlis.remove(int(n))
        
        for i in numlis:
            dfs(v+1, str(arr) + str(i))
            

             
dfs(0, "")

