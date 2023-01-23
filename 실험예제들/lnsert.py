import sys
sys.stdin=open("실험예제들/insert.txt", "rt")


# 정수 1234567 을 정수들의 리스트인 [1, 2, 3 ,4 , 5 ,6 ,7] 로 변환하여라 

n = int(1234567)

lst = list(map(int, str(n)))

print(lst)