import sys
sys.stdin=open("2.txt", "rt")


def getnumdivsior(n):
    cnt = 0
    for i in range(1, n+1):
        if n%i == 0:
            cnt += 1 
    return cnt

    


def getnumfrom(str):
    num = ''
    for c in str:
        if c.isdecimal():
            num = num + c
    num = int(num)

    return num

#print(getnumfrom(s))
#print(getnumdivior(12))

s = input()

n = getnumfrom(s)
num = getnumdivsior(n)




# 자연수 출력 

print(n)

# 약수의 갯수 출력 

print(num)