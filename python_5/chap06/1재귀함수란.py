import sys

sys.stdin=open("chap06/1.txt", "r")

n = int(input())


def div2(n):
    q = n // 2 
    r = n % 2


    if q == 1:
        print(q, end="")
        print(r, end="")
    else:
        div2(q)
        print(r, end="")


div2(n)