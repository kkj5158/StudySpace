import sys
sys.stdin=open("chap03/5.txt", "rt")

n, m = map(int, input().split())

def sum(a, i, j):
    sum = 0

    while i!=j+1:
        sum += a[i]
        i +=1
    return sum

a = []

a.append(0)

a = a + list(map(int, input().split()))

#print(a)

count = 0

for i in range(1,n+1):
    for j in range(i, n+1):
        if sum(a, i, j) == m :
            count += 1


print(count)
