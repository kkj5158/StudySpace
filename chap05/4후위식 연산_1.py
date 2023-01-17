import sys
sys.stdin=open("chap05/4.txt", "r")

arr = input()

num = []

for a in arr:
    if a.isdecimal():
        num.append(a)
    else :
        b1 = int(num.pop())
        b2 = int(num.pop())

        if a == '+':
            result = b2 + b1
        elif a == '-':
            result = b2 - b1
        elif a == '/':
            result = b2 / b1
        elif a == '*':
            result = b2 * b1
        
        num.append(result)

c = num.pop()

print(c)
       


# 352+*9-
# 37*9-
# 21 9 - 
# 12  

# 3 5 2

# 3 7 

# 21

# 21 9

# 12

# 숫자이면은 푸쉬한다. 연산자를 만나면 pop을 2번한다. pop한 두개의 원소를 연산자로 계산한다. 계산된 원소를 푸쉬한다.

# num에서 pop 2번 , acc에서 pop-1개 계산하고 다시 푸쉬

# 3 7

# *

# 3 10 9 

# 3 