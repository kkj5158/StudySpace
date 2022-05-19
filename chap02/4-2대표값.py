import sys
sys.stdin=open("chap02/4.txt", "rt")

n = int(input())

a = list(map(int, input().split()))

avg = round(sum(a)/len(a))

def getdistance(x):
    if(x-avg)<0:
        return abs(x-avg)+1 # 거리차가 음수이면 보정값 1을 더해서 우선순위를 뒤로 미룬다 . 
    else:
        return abs(x-avg) 
    

c = list(map(getdistance, a))

min = float('inf')

for num in c:
    if num<min:
        min = num
    

print(avg, c.index(min)+1)
    
