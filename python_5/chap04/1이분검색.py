import sys
sys.stdin=open("chap04/1.txt", "rt")

n , m = map(int, input().split())

a = list(map(int,input().split()))

a.sort()

start = 0
end = n-1

mid = (start+end)//2

while True:
    if a[mid] == m:
        print(mid+1)
        break
    elif m < a[mid] :
        end = mid-1
        mid = (start+end)//2
    elif m > a[mid] :
        start = mid+1
        mid = (start+end)//2


# 0  1  2  3  4  5  6  7
# 12 23 32 57 65 81 87 99



