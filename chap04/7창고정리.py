import sys
sys.stdin=open("chap04/7.txt", "rt")

def move(lis, size):
     # 첫번째로 큰 값과 두번째로 큰 값의 차이를 구한다.
    lis[size-1] = lis[size-1]-1
    lis[0] = lis[0] + 1
    


l = int(input())

mp = list(map(int, input().split()))

n = int(input())

mp.sort()

#print(mp)

for _ in range(n):
    move(mp, l)
    mp.sort()

print(mp[l-1]-mp[0])

