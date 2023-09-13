import sys
sys.stdin=open("chap08/1.txt", "rt")

n = int(input())

dy = [0]*(n+1)

dy[1]=1
dy[2]=2

#dy[3] = 3 
#dy[4] = 5

for i in range(3, n+1):
  dy[i]=dy[i-1]+dy[i-2]


print(dy[n])


