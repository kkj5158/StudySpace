import sys
sys.stdin=open("chap05/2.txt", "r")

s = input()

stack = []

# ()

#  0

#  ((((

# (())

# 스택에 무엇이 들어올때 어떻게 작동할것인지에 대한 이해하가

# 이전 꺼 vs 다음 꺼 
# ( ( -> stack에 push한다.  ( -> push
# ( ) -> (레이저생성) (막대생성) stack에서 pop한다. stack(len) 갯수만큼 더하기 ) -> pop
#  ) ) -> 나머지 막대가 하나 잘린다. -> +1 
# ) (  -> 
# 
#   0
# ((( -> 3
# ((( -> 3
# ) -> 1
# ((( -> 3
# ) -> 1
# (( -> 2
# ) -> 1
# ) -> 1
# -> 1
# -> 1
cnt = 0

for i in range(len(s)):
    if s[i] == '(':
        stack.append(i)
    elif s[i] == ')':
        if s[i-1] == '(':
            stack.pop()
            cnt = cnt + len(stack)
        elif s[i-1] == ')':
            stack.pop()
            cnt = cnt  + 1
                   
                
print(cnt)            