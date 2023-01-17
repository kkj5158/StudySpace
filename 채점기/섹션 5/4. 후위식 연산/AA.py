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
       
