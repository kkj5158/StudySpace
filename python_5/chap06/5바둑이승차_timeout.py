import sys

sys.stdin=open("chap06/5.txt", "r")

m, n = map(int, input().split())

lis = [[0,0] for _ in range(n)]

#[[무게, 탑승여부]]

for i in range(n):
    lis[i][0] = int(input())


sumarr = []

def dfs(v):
    total = 0
    if v == n:
        for w , st in lis:
            if st==1:
                total = total + w
        
        if total <= m:
            sumarr.append(total)

    else: 
        lis[v][1] = 0
        dfs(v+1)
        lis[v][1] = 1
        dfs(v+1) 
                
        


dfs(0)

print(max(sumarr))

