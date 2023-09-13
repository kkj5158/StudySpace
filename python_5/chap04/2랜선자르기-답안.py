import sys
sys.stdin=open("chap04/2.txt", "rt")

# count 함수 
def Count(len):
    cnt = 0
    for x in Line:
        cnt += (x//len)
    return cnt

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

while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)>=n:
        res = mid
        lt=mid+1
    else:
        rt=mid-1
        
print(res)


"""
lt = mid , rt = mid 가 아니라 lt=mid+1 , rt=mid+1 로 코드를 작성하고 나서 , lt>rt 일 경우에 반복문을 멈추면 된다.
->lt가 rt 보다 커지는 경우는 탐색이 끝난경우이다. 
"""

