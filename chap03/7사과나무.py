import sys
sys.stdin=open("chap03/7.txt", "rt")

n = int(input())

# 이런 형식 연습해두기 
map = [list(map(int,input().split())) for _ in range(n)]

mid = n // 2

l = mid
r = mid + 1

total = 0 

for i in range(n):
    total += sum(map[i][l:r])
    if i < mid:
        l = l-1
        r = r + 1
    else:
        l = l+1
        r = r-1


print(total)


# 10
# 92 
# 154
# 349
# 