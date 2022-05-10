import sys
sys.stdin=open("6.txt", "rt")

n = int(input())

# 2차원 배열로 매핑 

map = [list(map(int, input().split())) for _ in range(n)]

lst = 0


# 행과 열의 합 
for i in range(n):
    sum1 = 0
    sum2 = 0
    for j in range(n):
        sum1 += map[i][j]
        sum2 += map[j][i]

    if sum1 > lst:
        lst = sum1
    
    if sum2 > lst:
        lst = sum2


# 대각선의 합 

sum1 = 0
sum2 = 0

for i in range(n):

    sum1 += map[i][i]
    sum2 += map[n-i-1][n-i-1]

    if sum1 > lst:
        lst = sum1
    
    if sum2 > lst:
        lst = sum2

print(lst)