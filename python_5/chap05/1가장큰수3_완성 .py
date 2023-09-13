from inspect import stack
import sys
sys.stdin=open("chap05/1.txt", "rt")

arr , cnt = map(int, input().split())

arr = list(map(int, str(arr)))

stack = []

stack.append(arr[0])

max = stack[0]

# tos 개념 활용하기 


# 5276823 

# 5

# 52 

# 527  3 

# 7 1 

# 76 1 

# 768 1

# 78 0 

# 7823

# max라는 개념을 도입시에 문제가 너무 복잡해짐 언제나 간단하게 생각하기. 
# max라는 개념은 stack을 도구로 사용하는 도구적 관점과 맞지 아닌한다. 
# tos라는 개념으로 접근하기 , stack.peek()

# tos와 입력값을 비교한다. 
# tos보다 입력값이 클경우 pop을 실행한다
# 카운트를 감소시킨다. 
# 갱신된 tos와 입력값을 비교하여 클 경우 pop을 실행한다. 
# 조건이 성립하지 않을시 append한다. 


for i in arr[1:]:
            
    while len(stack) > 0 and stack[-1] < i and cnt > 0:
        stack.pop()
        cnt = cnt -1 
    stack.append(i)


# cnt가 남았을경우 뒤의 숫자를 모두 없앤다. 
while cnt>0:
    stack.pop()
    cnt = cnt -1;

print(*stack, sep='')

# exit code 해결하기 
