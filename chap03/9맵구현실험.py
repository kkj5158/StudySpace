import sys
sys.stdin=open("9.txt", "rt")


n = int(input())


# 맵 세팅 

mp = []

mp = [list(map(int, input().split())) for _ in range(n)]

wall = [0]*n

mp.insert(0,wall)
mp.append(wall)

for x in mp:
    x.insert(0,0)
    x.append(0)


print(mp)
# 이런 접근 방식은 너무 까다롭다. 






# 맵 구현하기 