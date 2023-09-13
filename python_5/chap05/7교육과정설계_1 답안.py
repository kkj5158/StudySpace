from collections import deque
import sys

sys.stdin=open("chap05/7.txt", "r")

def isorderequal(a, b):

    r = []

    for i in range(len(a)):
        r.append(a[i]==b[i])

    if all(r):
        return True
    else:
        return False



must = deque(input())

n = int(input())

lst = []

for i in range(n):
    lst.append(input())


# 리스트로 반복한다. 

# 필수과목이면서 , 큐에 들어가 있지 않은 경우 큐에 집어넣는다 . (중복제거)

# 원소인지 아닌지 사용하는 함수 알아보기 

# 



# 모두 들어가 있는가 
# 길이를 서로 비교한다. -> 길이가 동일하면 모두 들어가 있음



# 순서가 지켜져 있는가 
# for문을 돌린다. (갯수가 동일하므로) , 서로 pop한다. pop해서 모두 비교한다. 
# 비교결과가 모두 참일경우

# 마지막으로 YES 

# 그외의 경우는 모두 no로 처리한다. 

cnt=0

for i in range(len(lst)):

    chq = deque()


    cnt = cnt + 1

    for j in lst[i]:
        if any(j == i for i in must) and all(j != i for i in chq):
            chq.append(j)
    
    if len(chq) == len(must) and isorderequal(chq, must):
        print("#" + str(cnt) + " YES")
    else:
        print("#" + str(cnt) + " NO")

        


