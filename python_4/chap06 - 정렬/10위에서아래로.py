import sys
sys.stdin=open("chap06 - 정렬/10.txt", "rt")


n = int(input())

numarray = []

for i in range(n):
    numarray.append(int(input()))

numarray.sort(reverse=True)

print(numarray)

