import sys
sys.stdin = open("basic/200자료구조/1.txt")

n = int(input())


comm = []
stack = []

# push 명령어는 어떻게 처리할 것인가 

for _ in range(n):
    comm.append(list(map(str,input().split())))

# 스택에 집어넣기 . 빼기 명령어들 실행 . 

for x in comm:
    c , d = map()
    


print(comm)