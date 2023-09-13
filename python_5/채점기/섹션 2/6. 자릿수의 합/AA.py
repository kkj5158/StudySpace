n = int(input())

m = list(map(int, input().split()))

def digit_sum(x):
    sum = 0
    
    while x != 0:
        r = x % 10
        x = (x-r) // 10
        sum += r
    
    return sum

max = 0
maxnum = 0

for i in m:
    isum = digit_sum(i)
    if isum>max : 
        max = isum
        maxnum = i

print(maxnum)
