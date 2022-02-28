# 연산을 사용하는 회수 -> 큰수로 최대한 나눈다. 5로 나눈다가 가장 먼저 선택해야하는 선택지이다, 

"""
44 -> 22 -> 11 -> 10 -> 2 -> 1 5 
44 -> 22 -> 21 -> 20 -> 4 -> 2 -> 1
47 -> 46 -> 45 -> 9 -> 8 -> 4 -> 2 -> 1
        -> 23 -> 22 ->11 -> 10 -> 2 -> 1 

연산의 우선순위 적용 

1 . 5 , 3 , 2, 그래도 적용이 안된다면 1로 뺀다. 

"""

n = int(input())

result = n
count = 0 

while result != 1:
    if result & 5 == 0:
        result = result / 5
        count = count + 1
    elif result & 3 == 0:
        result = result / 3
        count = count + 1
    elif result & 2 == 0:
        result = result / 2
        count = count + 1
    else:
        result = result - 1
        count = count + 1

    

print(count)

"""
이렇게 연산의 우선순위로 접근하면 , 잘못된 답이 나오게 된다. 
다이나믹 프로그래밍 알고리즘으로 접근하자 . """