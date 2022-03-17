
n = int(input())
list = list(map(int, input().split()))

list.sort()

count = 0
group = 0

for i in list:
    count += 1 
    if count >= i :
        group += 1
        count = 0

print(group)