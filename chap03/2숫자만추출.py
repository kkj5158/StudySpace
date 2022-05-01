from curses.ascii import isalpha
import sys
sys.stdin=open("2.txt", "rt")

s = input()

    



#def getdivior(n):


def getnumfrom(str):
    num = ''
    for c in str:
        if c.isdigit():
            num = num + c
    
    int(num)

    return num

print(getnumfrom(s))


# 자연수 출력 

print()

# 약수의 갯수 출력 

print()