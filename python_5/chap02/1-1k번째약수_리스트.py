import sys
sys.stdin=open("chap02/1.txt", "rt")

n , k = map(int, input().split())

nums = [-1]*(n+1)

cnt = 1

for i in range(1,n+1):
    if n%i == 0:
        nums[cnt] = i
        cnt+=1

print(nums[k])