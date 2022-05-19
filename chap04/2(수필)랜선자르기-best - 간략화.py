
import sys
sys.stdin=open("chap04/2.txt", "rt")

k, n = map(int, input().split())

a = []

for _ in range(k):
    a.append(int(input()))

#print(a)

#print(802 + 743 + 457 + 539) # 2541
#print(2541//11) # 231


lt = 1 # 1

rt = sum(a)//n # 231 

mid = (lt+rt)// 2 # 116  

# 최대값을 찾아야 한다 . max 치로 계산하기 


lar = 0

while True:

    cnt = 0

    for l in a :
        cnt += l//mid
    
    if cnt >= n:
        lar = max(mid, lar)
        lt = mid
        mid = (lt+rt)//2
    
    elif cnt < n :
        rt = mid
        mid = (lt+rt)//2

# 탈출 조건 생각하기 
    if mid==lt or mid == rt:
        break
        

print(lar)

# 문제는 답이 하나가 아니다라는 부분이구나 . 





    
    