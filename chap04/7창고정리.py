import sys
sys.stdin=open("chap04/7.tx0t", "rt")

def move(lis, size, ):
    cnt = lis[size-1] - lis[size-2]
     # 첫번째로 큰 값과 두번째로 큰 값의 차이를 구한다.
      
    


l = int(input())

mp = list(map(int, input().split()))

n = int(input())

mp.sort()

print(mp)

for _ in range(n):
    