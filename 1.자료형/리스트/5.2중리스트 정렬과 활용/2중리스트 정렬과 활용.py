
array = [[50, "apple"], [30, "banana"] , [400, "melon"]]

print(array)

# int를 기준으로 정렬하기 

array.sort(key=lambda x:x[0])

print(array)


# int를 기준으로 정렬하기 -> -를 붙이면 역순으로 정렬이 가능하다 
# 기본정렬은 언제나 오름차순, -를 붙이면 역순인 내림차순으로 정렬이 가능하다. 

array.sort(key=lambda x:-x[0])

print(array)

# str를 기준으로 정렬하기 

array.sort(key=lambda x:x[1])

print(array)

# int를 첫번째키로, str를 두번째 키로 정렬하기 

array.sort(key=lambda x:[x[0], x[1]])

print(array)

# str를 첫번째키로, str를 두번째 키로 정렬하기 
array.sort(key=lambda x:[x[1], x[0]])

# x[1] -> str이 가장 높은 우선순위가 되고 x[0] 가 두번째 우선순위가
# 되어라  ! 

