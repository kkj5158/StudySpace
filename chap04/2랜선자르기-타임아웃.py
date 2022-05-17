import sys
sys.stdin = open("2.txt")

k, n = map(int, input().split())

a = []

for _ in range(k):
    a.append(int(input()))

#print(a)

#print(802 + 743 + 457 + 539) # 2541
#print(2541//11) # 231

total = sum(a)

elen = total // n



while True:
    cnt = 0
    for l in a:
        cnt += l//elen
    
    if cnt >= n:
        print(elen)
        break
    else:
        elen = elen - 1


        

    
    