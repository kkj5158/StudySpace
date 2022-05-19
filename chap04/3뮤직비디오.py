import sys
sys.stdin=open("chap04/3.txt", "rt")

n, m = map(int, input().split())

a = list(map(int, input().split()))


total = sum(a)

lt = total//m


 

