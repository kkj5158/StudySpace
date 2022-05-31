import sys
sys.stdin=open("chap04/4.txt", "rt")

n, c = map(int, input().split())

mp = []
dis = []

for _ in range(n):
    mp.append(int(input()))

mp.sort()

#print(mp)

# 1 2 4 8 9 13 15 25 50 57 100 
# 1 2 3 4 5 6 7 8 9 10 100
# 인덱스 개념이 아니라 거리 개념에서의 중앙 

lt = 1
rt = mp[n-1] - mp[0]
mid = (lt+rt)//2 # 가장 가까운 두말의 최대 거리 

#1
#4 
#8

# 말 배치 시작 

# 알고리즘의 순서 

# 1 mid 값에 맞춰서 0 인덱스부터 말들을 뛰어서 배치한다. 
# 2 말들이 미드값에 맞춰서 순서대로 모두 배치되는 경우 -> 미드값을 키운다  . ( 더 높은 값을 찾기 위해서 )
# 3 말들이 미드값에 맞춰서 순서대로 배치되는 와중에 인덱스를 넘어가는 경우 -> 미드값을 낮춘다 . (더 낮은 값들중에서 탐색하여서 가장 높은 값을 찾는다. ) 

max = 0

while lt < rt:
    x = 0

    for _ in range(c):

        y = x+1

        if y > n-1: 
    # mid의 값이 너무 크다 
            rt = mid - 1
            mid = (lt+rt)//2
            break
            
        dis = mp[y] - mp[x]
        # 최대값을 만족한다 
        if dis >= mid:
            x = y
            # 말을 배치하고 다음 말을 배치하러 반복문을 진행시킨다. 
            continue
        # 최대값을 만족하지 않고 거리가 부족하다 
        else:
            y = x+1


while lt < rt:

    x = 0

    for _ in range(c):

        y = x+1

        while True:
            

    



    # 최대값을 만족한다. 
        
    
    







# 답지 말고도 해당과정에서 생각의 과정을 충분히 정리해서 접근해보기 



