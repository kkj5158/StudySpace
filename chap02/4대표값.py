import sys
sys.stdin=open("4.txt", "rt")

n = int(input())

a = list(map(int, input().split()))

avg = round(sum(a)/len(a))

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
    
