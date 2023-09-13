import sys
sys.stdin=open("chap04 - 구현/2.txt", "rt")

# 시간, 분 , 초 따로따로 입력받기 
# 3중 for문 작성해서 count 세기 
# 
n = int(input())

count = 0

for h in range(n+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h) + str(m) + str(s):
                count = count + 1

print(count)
            
    