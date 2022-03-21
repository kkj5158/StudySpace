
n = int(input())
nlist = list(map(int, input().split()))

count = 0
result = 0 

nlist.sort()

for i in nlist:
    count += 1
    if count >= i:
        result += 1 
        count=0

print(result)

