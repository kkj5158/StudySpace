import sys
sys.stdin=open("8.txt", "rt")

n = int(input())

mp = []

mp.append([0]*n)

for _ in range(n):
    mp.append(list(map(int, input().split()))) # 1행부터 시작 고려하기 

print(mp)

m = int(input())

#print(m)

moves = [list(map(int, input().split())) for _ in range(m)]

print(moves)