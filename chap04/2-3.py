# 시간, 분 , 초 따로따로 입력받기 
# 3중 for문 작성해서 count 세기 
# 

n = int(input())

count = 0 

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)        


    