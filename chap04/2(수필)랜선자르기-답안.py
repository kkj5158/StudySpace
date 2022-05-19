import sys
sys.stdin=open("chap04/2.txt", "rt")

# count 함수 
def Count(len):
    cnt = 0
    for x in Line:
        cnt += (x//len)

k, n = map(int, input().split())

Line = []

res = 0

largest = 0

for i in range(k):
    tmp = int(input())
    Line.append(tmp)
    largest = max (largest, tmp)

# best 하고 lt 와 rt 에 대한 생각이 다른 이유는 ???? 

lt = 1
rt = largest

while lt>=rt:
    mid=(lt+rt)//2
    if Count(mid)>=n:
        res = mid
        lt=mid+1
    else:
        rt=mid-1
        
print(res)



