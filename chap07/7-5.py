# 이진탐색 알고리즘은 반드시 암기 해두기 !!! 

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end)//2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
        return None


num = int(input())

goods = list(map(int, input().split()))

goods.sort()

#print(goods)

fnum = list(map(int, input().split()))

fgoods = input().split()


for i in x:
    result = binary_search(goods, i, 0, num-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')
