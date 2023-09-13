import sys
sys.stdin=open("8.txt", "rt")

n = int(input())

mp = [list(map(int, input().split())) for _ in range(n)]

print(mp)

m = int(input())

print(m)

moves = [list(map(int, input().split())) for _ in range(m)]

print(moves)


# moves 실행하기 


for move in moves:
    row , dir , num = map(lambda x:x, move) # map 의 언팩킹 기능 사용 # x는 단순히 x로 변환한다. 
    print(row, dir, num)



"""

list is not callable -> 함수와 같은 이름의 변수 사용하지 말기 . 

"""