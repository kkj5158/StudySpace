import sys

sys.stdin=open("chap06/8.txt", "r")

n, m = map(int, input().split())

# arr = [0 for _ in range(m)]

chk = [0 for _ in range(n+1)]

def dfs(v):
    global n 

    if v==m:
        for pos, val in enumerate(chk[1:], 1):
            if val==1:
                print(pos, end="")
        print()
                
    else:
        numlis = [j for j in range(1, n+1)]

        for pos, val in enumerate(chk):
            if val==1:
                numlis.remove(int(pos))
                
        
        for num in numlis:
            chk[num] = 1
            dfs(v+1)
            
                         
dfs(0)

