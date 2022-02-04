# 입력 구현하기 
# 좌표값 구현하기 -> 알파벳을 좌표로 변환시키기 
# 나이트의 이동값 구현하기 
# 나이트의 모든 이동 경우의 수 구하기 
# 더했을때의 좌표값이 맵을 넘어가지 않는지 여부 판단하기 
# 넘어가지 않았을때에만 카운트 올리기 

area = input()
row = int(area[1])
column = int(ord(area[0])) - int(ord('a')) + 1 # 좌표값구현하기 -> 알파벳 좌표로 변환하기 ! 

steps =  [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

count = 0 

for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]

    if next_row >=1 and next_row <= 8 and next_column >=1 and next_column<=8:
        count +=1

print(count)