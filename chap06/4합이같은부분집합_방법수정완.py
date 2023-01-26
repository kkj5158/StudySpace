import sys

sys.stdin=open("chap06/4.txt", "r")

n = int(input())

nums = list(map(int,input().split()))

isin = [ [0, 0] for _ in range(n)]

# [숫자 , 참여여부] 0이면 미참 1이면 참여 

for pos, val in enumerate(nums):
    isin[pos][0] = val

starr = []

# print(isin)
# 


def dfs(v):

    if v == n :
        total1 = 0
        total2 = 0

        for num, st in isin:
            if st == 1 :
                total1 = total1 + num
            else:
                total2 = total2 + num
        
        if total1 == total2:
            starr.append(True)
        else:
            starr.append(False)
    else:
        isin[v][1] = 1
        dfs(v+1)
        isin[v][1] = 0
        dfs(v+1)   


dfs(0)

if any(starr):
    print("YES")
else :
    print("NO")