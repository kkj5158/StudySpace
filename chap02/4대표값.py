import sys
sys.stdin=open("chap02/4.txt", "rt")

n = int(input())

a = list(map(int, input().split()))

#avg = round(sum(a)/len(a))

#round는 round_half_even 방식을 택한다 -> 64.5 -> 64 (짝수에 가깝게 반올림 )
# 이 경우를 대비해서 , 다음과 같이 반올림 시킨다. 

avg = sum(a)/len(a)

avg = avg + 0.5 

avg = int(avg) 

# int 가 반올림 과정을 올바르게 수정해준다. 


c = list(map(lambda x: x-avg, a))

pnums = []
mnums = []

for num in c :
    if(num<0):
        mnums.append(num)
    else:
        pnums.append(num)

pnums.sort()
mnums.sort(reverse=True)

min = 0

if abs(pnums[0])==abs(mnums[0]):
    min = pnums[0]
elif abs(pnums[0])<abs(mnums[0]):
    min = pnums[0]
else:
    min = mnums[0]

print(avg, c.index(min)+1)
    
