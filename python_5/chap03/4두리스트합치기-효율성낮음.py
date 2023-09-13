import sys
sys.stdin=open("chap03/4.txt", "rt")

n1 = int(input())

a1 = list(map(int, input().split()))

n2 = int(input())

a2 = list(map(int, input().split()))

# 리스트 합치기 

# 리스트 정렬 


a = a1 + a2

a.sort()

print(*a)