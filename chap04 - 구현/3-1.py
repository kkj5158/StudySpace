#  좌표 입력받기 

# end 이동가능한 경우의 수 출력하기 


import sys
sys.stdin=open("chap04 - 구현/3.txt", "rt")

loc = input()

x = ord(loc[0]) - ord('a') + 1
y = int(loc[1])

count = 0 

#좌표 구현하기 

"""
x = [1, 2, 3, 4 ,5 ,6 ,7 ,8]
y = [1, 2, 3, 4, 5, 6, 7, 8]
"""

# 어떻게 a를 1로 생각할것인가 > -> 아스키 코드의 문제 

moves = [[2,1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]

for i in range(len(moves)):
    nx = x + moves[i][0]
    ny = y + moves[i][1]
    if(nx > 0 and nx < 9 and ny>0 and ny<9):
        count = count + 1


print(count)






