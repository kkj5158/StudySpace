import sys
sys.stdin = open("basic/200자료구조/2.txt")

n = int(input())

sep = " "

for _ in range(n):
    a = input()
    
    a = a + " "
    
    lis = []

    for s in a:
        if s!=sep:
            lis.append(s)
        else:
            for _ in range(len(lis)):
                print(lis.pop(), end='')
            
            print(sep, end='')

    print()



