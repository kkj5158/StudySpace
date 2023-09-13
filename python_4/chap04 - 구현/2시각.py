import sys
sys.stdin=open("chap04 - 구현/2.txt", "rt")

h = int(input())

count = 0 

for i in range(h+1):
    for j in range(60):
        for k in range(60):

            if '3' in str(i) + str(j) + str(k):
                count +=1 

print(count)