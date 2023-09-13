import sys

sys.stdin=open("chap06/5.txt", "r")

m, n = map(int, input().split())

lis = []

for _ in range(n):
    lis.append(int(input()))


result = 0
total = sum(lis)

def DFS(v, sum, tsum):
    global result
    global total 
    
    if sum + (total - tsum) < result :
        return
    if sum > m:
        return
    if v == n:
        if result < sum:
            result=sum
    else:
        DFS(v+1, sum,tsum+lis[v] )
        DFS(v+1, sum+lis[v], tsum+lis[v])


DFS(0,0,0)

print(result)

