import sys
sys.stdin=open("6.txt", "rt")

n = int(input())

m = list(map(str, input().split()))

max = 0
index = 0 

for i, s in enumerate(m):
    sum = 0
    for j in range(len(s)):
        sum += int(s[j])

    if sum > max :
        max = sum
        index = i

print(m[index])
  
       