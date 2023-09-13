import sys

sys.stdin=open("chap06/4.txt", "r")

n = int(input())

nums = list(map(int, input().split()))

chkarr = [ [0,0] for _ in range(n+1)]

for i, val in enumerate(nums):
    chkarr[i][0] = val

tfarr = []

def dfs(v):
    

    if v == n+1:
        sum1=0
        sum2=0

        for num, chk in chkarr:
            if chk == 1:
                sum1 = sum1 + num
            elif chk == 2:
                sum2 = sum2 + num
        
        if sum1!=0 and sum2!=0 and sum1 == sum2 :
            tfarr.append(True)
        
    else:
        chkarr[v][1] = 0
        dfs(v+1)
        chkarr[v][1] = 1
        dfs(v+1)
        chkarr[v][1] = 2
        dfs(v+1)    


dfs(1)

if any(tfarr):
    print("YES")
else:
    print("NO")