
n = int(input())
nlist = list(map(int, input().split()))

count = 0
result = 0 

nlist.sort()

for i in nlist:
    count += 1
    if count >= i:
        result += 1 
        count=0

print(result)

# 지옥 같네 

    

# for문과 함께 자주 사용하는 range 함수
# for문은 숫자 리스트를 자동으로 만들어 주는 range 함수와 함께 사용하는 경우가 많다. 다음은 range 함수의 간단한 사용법이다.
# 모두 하나하나 체크해나가기 

# >>> a = range(10)
# >>> a
# range(0, 10)
# range(10)은 0부터 10 미만의 숫자를 포함하는 range 객체를 만들어 준다.

# 시작 숫자와 끝 숫자를 지정하려면 range(시작 숫자, 끝 숫자) 형태를 사용하는데, 이때 끝 숫자는 포함되지 않는다.

# >>> a = range(1, 11)
# >>> a
# range(1, 11)
# range 함수의 예시 살펴보기
# for와 range 함수를 사용하면 1부터 10까지 더하는 것을 다음과 같이 쉽게 구현할 수 있다.

# >>> add = 0 
# >>> for i in range(1, 11): 
# ...     add = add + i 
# ... 
# >>> print(add)
# 55
# range(1, 11)은 숫자 1부터 10까지(1 이상 11 미만)의 숫자를 데이터로 갖는 객체이다. 따라서 위 예에서 i 변수에 리스트의 숫자가 1부터 10까지 하나씩 차례로 대입되면서 add = add + i 문장을 반복적으로 수행하고 add는 최종적으로 55가 된다.

# 또한 우리가 앞에서 살펴본 "60점 이상이면 합격"이라는 문장을 출력하는 예제도 range 함수를 사용해서 바꿀 수 있다. 다음을 보자.
# #marks3.py
# marks = [90, 25, 67, 45, 80]
# for number in range(len(marks)):
#     if marks[number] < 60: 
#         continue
#     print("%d번 학생 축하합니다. 합격입니다." % (number+1))
# len 함수는 리스트 안의 요소 개수를 돌려주는 함수이다. 따라서 len(marks)는 5가 될 것이고 range(len(marks))는 range(5)가 될 것이다. number 변수에는 차례로 0부터 4까지의 숫자가 대입될 것이고, marks[number]는 차례대로 90, 25, 67, 45, 80 값을 갖게 된다. 결과는 marks2.py 예제와 동일하다.