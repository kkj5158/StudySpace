import sys

sys.stdin=open("chap06/5.txt", "r")

m, n = map(int, input().split())

lis = []

for _ in range(n):
    lis.append(int(input()))


max = 0

def DFS(v, sum):
    global max 


    if sum > m:
        return
    if v == n:
        if max < sum:
            max=sum
    else:
        DFS(v+1, sum)
        DFS(v+1, sum+lis[v])


DFS(0,0)

print(max)

