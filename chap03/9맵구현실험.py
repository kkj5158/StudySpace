import sys
sys.stdin=open("9.txt", "rt")


n = int(input())


# 맵 세팅 
mp = []

for _ in range(n+1):
    mp[0].append(0)

mp.append(list(map(int, input().split())) for _ in range(n))


print(mp)