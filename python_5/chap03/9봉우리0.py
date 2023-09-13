import sys
from turtle import right
sys.stdin=open("chap03/9.txt", "rt")


n = int(input())


# 맵 세팅 
mp = []

mp = [list(map(int, input().split())) for _ in range(n)]

for x in mp:
    print(x)

wall = [0]*n

mp.insert(0,wall)
mp.append(wall)

for x in mp:
    print(x)

# 맵 오류 해결하기 -> 왜 이런 방식으로 맵이 나오는지 . 

for x in mp:
    x.insert(0,0)
    x.append(0)





# 봉우리인지 아닌지 판단하기 

def ismountain(x, y):
    mid = mp[x][y]
    top = mp[x-1][y]
    bottom = mp[x+1][y]
    left = mp[x][y-1]
    right = mp[x][y+1]

    if mid>top and mid > left and mid>left and mid>right and mid >bottom:
        return True
    else:
        return False

cnt = 0 

for i in range(1,n):
    for j in range(1,n):
        if ismountain(i, j):
            cnt +=1
    
print(cnt)
    




"""
    i-1, j
i-1,j i,j  i+1,j
    i+1, j+1
"""

"""





"""
