
array = [[50, "apple"], [30, "banana"] , [400, "melon"]]

print(array)

# int를 기준으로 정렬하기 

array.sort(key=lambda x:x[0])

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

