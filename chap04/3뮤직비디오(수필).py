import sys
sys.stdin=open("chap04/3.txt", "rt")

n, m = map(int, input().split())

a = list(map(int, input().split()))


total = sum(a)

lt = total//m

#print(lt)

# 최악의 경우는 ??? 

lar = max(a)

rt = lar*n//m

#print(rt)

mid = (lt+rt)//2


total = 0
cnt = 0

sm = 100000000000

# 결정 알고리즘 구상하기 
while lt<=rt:

    for d in a:
        if(total+d > mid):
            cnt+=1
            total = 0
        total += d

    if(cnt==m):
        sm = min(sm, mid)
    elif(cnt > m):
        rt = mid + 1
        mid = (lt+rt)//2
    elif(cnt<m):
        lt = mid+1
        mid = (lt+rt)//2
        

print(sm)



    