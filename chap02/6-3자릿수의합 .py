import sys
sys.stdin=open("chap02/6.txt", "rt")

n = int(input())

m = list(map(int, input().split()))

def digit_sum(x):
    sum = 0
    for i in str(x):
        sum+=int(i)
    return sum


max = 0

for i in m:
    sum = digit_sum(i)
    if sum > max :
        max = sum
        maxi = i
        
     
print(maxi)
    