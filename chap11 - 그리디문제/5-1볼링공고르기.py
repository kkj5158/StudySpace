import itertools

n, m = map(int, input().split())

weights = list(map(int, input().split()))

clist = list(itertools.combinations(range(0, n),2))

all = len(clist)

count = 0

for (i, j) in clist:
    if weights[i]==weights[j]:
        count += 1

result = all - count 

print(result)