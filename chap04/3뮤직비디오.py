import sys
sys.stdin=open("chap04/3.txt", "rt")


n, m = map(int, input().split())

a = list(map(int, input().split()))

total = sum(a)

#print(lt)

# 최악의 경우는 ??? 

lt = 1

rt = sum(a)

#print(rt)

mid = (lt+rt)//2

sm = 100000000000


# 결정 알고리즘 구상하기 

while lt<=rt:

    total = 0
    cnt = 1

    for d in a:
        if(total+d > mid):
            cnt+=1
            total = 0
        total += d


    if cnt<=m:
        sm = min(sm, mid)
        rt = mid - 1
        mid = (lt+rt)//2
    elif cnt>m:
        lt = mid + 1
        mid = (lt+rt)//2
        

# 오류 수첩 -> cnt는 기본이 1개이다. 

print(sm)



    