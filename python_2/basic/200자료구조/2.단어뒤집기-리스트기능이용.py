import sys
sys.stdin = open("basic/200자료구조/2.txt")

n = int(input())

for _ in range(n):
    a = list(input().split())

    for s in a:
        print(s[::-1], end=' ')

    print()




    