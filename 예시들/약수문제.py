
import sys

sys.stdin=open("input.txt", "rt")

n , k = map(int, input().split)


nums = []

for i in range(n):
    if n%i == 0:
        nums.append(i)

print(nums(k-1))