
n = int(input())

a = list(map(int, input().split()))

score = 1
total = 0


for s in a:
    if s == 1:
        total = total + score 
        score += 1
    else:
        score = 1


print(total)