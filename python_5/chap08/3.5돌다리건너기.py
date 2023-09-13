import sys
sys.stdin=open("chap08/1.txt", "rt")

# d[1] = 2
# d[2] = 3
# d[3] = 5

# 1 1 
# 2

# 1 1 1
# 2 1 
# 1 2
 
 # d[v] = d[v-1] + d[v-2]

n = int(input())

d = [0]*(n+1)

d[1] = 2
d[2] = 3

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])