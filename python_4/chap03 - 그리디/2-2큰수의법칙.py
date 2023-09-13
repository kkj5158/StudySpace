import sys
sys.stdin=open("chap03 - 그리디/2.txt", "rt")
# 입력 구현하기 
# 배열 정렬하기 
# 두번째 숫자 덧셈 횟구 구하기 -> m // k + 1 
# 첫번째 숫자 덧셈 횟수 구하기 -> n - 두번째 숫자 덧셈횟수
# result = +++ 

n , m, k = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()

result = 0

first = numbers[n-1]
#print(first)
second = numbers[n-2]
#print(second)

counts = m //(k+1) 
countf = m - m//(k+1)

#print(counts)
#print(countf)


result = first * countf + second * counts

print(result)

