import sys
sys.stdin=open("9.txt", "rt")


n = int(input())


# 맵 세팅 

mp = []

mp = [list(map(int, input().split())) for _ in range(n)]

wall = [0]*(n+2)

print(wall)

print(mp)

# 맵 구현하기 