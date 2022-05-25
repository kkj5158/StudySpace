import sys
sys.stdin=open("chap04/4.txt", "rt")

    

n, c = map(int, input().split())

mp = []
dis = []

for _ in range(n):
    mp.append(int(input()))

mp.sort()

#print(mp)

# 1 2 4 8 9 13 15 25 50 57 100 
# 1 2 3 4 5 6 7 8 9 10 100
# 인덱스 개념이 아니라 거리 개념에서의 중앙 

lt = 1
rt = 





