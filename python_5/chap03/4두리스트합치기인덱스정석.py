import sys
sys.stdin=open("chap03/4.txt", "rt")

n = int(input())

a = list(map(int, input().split()))

m = int(input())

b = list(map(int, input().split()))

c = []

aid = 0

bid = 0

count = 0 

while aid < n and bid < m:
    if a[aid] <= b[bid]:
        c.append(a[aid])
        aid += 1
        count += 1
    else:
        c.append(b[bid])
        bid += 1
        count += 1


if aid<n:
    c = c+a[aid:]

if bid<m:
    c = c+b[bid:]

for x in c :
    print(x, end=' ')