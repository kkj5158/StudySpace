import sys
sys.stdin=open("6.txt", "rt")

n = int(input())

# 2차원 배열로 매핑 

map = [list(map(int, input().split())) for _ in range(n)]


max = 0

# 각행의 합 

for x in map:
    if sum(x) > max :
        max = sum(x)
        
# 각 열의 합 


for i in range(n):
    sum = 0
    
    for j in range(n):
        sum += map[j][i]

    if sum > max:
        max = sum    

# 각 대각선의 합 

# 각 대각선의 합 알고리즘 다시한번 점검하기 

sum = 0

for i,j in zip(range(n), range(n)):
    sum += map[i][j]
    
if sum > max :
    max = sum

sum = 0

for i, j in zip(range(n-1,-1,-1), range(n-1,-1,-1)):
    sum += map[i][j]

if sum > max:
        max = sum 

print(max)
    
        
# 각 행의 합 구하기 , 각 열의 합 구하기 , 두 대각선의 합 구하기 

# https://ponyozzang.tistory.com/578
# -> zip 함수 사용 