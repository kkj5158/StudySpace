# 10 이하의 자연수 n을 받아서 주사위를 n번 던져서 나올 수 있는 모든 경우를 출력하라. 

import sys

sys.stdin=open("chap06/0.txt", "r")

n = int(input())

arr = [0 for _ in range(n)]


def dfs(v):
    for _ in range(n):
        if v==n:
            print(*arr)
            break
        else:
            for j in range(1,7):
                arr[v] = j
                dfs(v+1)
        

dfs(0)