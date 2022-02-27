# python for문의 range는 미만을 의미한다 for i in range(10) -> i는0~9 까지 변경된다. 

h = int(input())

count = 0

for i in range(h+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(i) + str(m) + str(s):
                count += 1
            
print(count)




# claer !! 