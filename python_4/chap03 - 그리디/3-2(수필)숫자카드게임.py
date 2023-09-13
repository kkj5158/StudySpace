import sys
sys.stdin=open("chap03 - 그리디/3.txt", "rt")

n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))

    min_value = 10001

    for a in data:
        if a < min_value:
            min_value = a


