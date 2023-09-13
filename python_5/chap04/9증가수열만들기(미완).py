from collections import deque
import sys
sys.stdin=open("chap04/9.txt", "rt")

n = int(input())

arr = list(map(int, input().split()))

arr = deque(arr)

arr2 = []

tmp = 0

while True:
    if arr[0] < tmp and arr[-1] < tmp:
        print(len(arr2))
        for i in range(len(arr2)):
            print[i][0]
        break        
    elif arr[0] > tmp :
        arr2.append(('L',arr[0]))
        tmp = arr[0]
        arr.popleft()
    elif arr[-1] > tmp :
        arr2.append(('R', arr[-1]))
        tmp = arr[-1]
        arr.pop()
      