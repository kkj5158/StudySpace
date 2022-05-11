import sys
sys.stdin=open("9.txt", "rt")


n = int(input())


# 맵 세팅 

mp = [list(map(int, input().split())) for _ in range(n)]

for _ in range(n+1):
    mp[0].append(0)


# 봉우리인지 아닌지 판단하기 

def ismountain(x, y):
    if 



"""
    i-1, j
i-1,j i,j  i+1,j
    i+1, j+1
"""

