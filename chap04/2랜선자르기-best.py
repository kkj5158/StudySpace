
import sys
sys.stdin = open("2.txt")

k, n = map(int, input().split())

a = []

for _ in range(k):
    a.append(int(input()))

#print(a)

#print(802 + 743 + 457 + 539) # 2541
#print(2541//11) # 231


lt = 1 # 1

rt = sum(a)//n # 231 

mid = lt+rt// 2 # 116  


while True:

    cnt = 0

    for l in a :
        cnt += l//mid
    
    if cnt == n:
        print(mid)
        break

    elif cnt > n:
        

    



    





    
    