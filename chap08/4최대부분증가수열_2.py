import sys
sys.stdin=open("chap08/4.txt", "rt")

# 연결이 아니라. 각자 생각하기 

# 8 이 마지막인 증가수열 

# 이전 숫자들중 가능한 최대수 + 1 

# 5 3 7 

# 중요한건 최대길이를 가지는 친구를 기억해두는일 

# 자기보다 작은 값들을 찾는다. 
# 자기보다 작은 값들이 없다면 최대길이는 1 이다. 

# 그 작은 값들중에 큰 길이를 가지는 친구를 찾는다 

# 그 길이에 +1을 하는것이 나의 최대길이이다. 

n = int(input())

nums = list(map(int, input().split()))

dp = [[0, 0] for _ in range(n+1)]


max = 0
totalmax=0

for pos, n in enumerate(nums, 1):
  if pos == 1:
    dp[pos][0] = n
    dp[pos][1] = 1
    totalmax = 1
  else:
    max = 0

    for (num, ln) in dp[:pos]: 
      if num < n:
        if ln > max:
          max = ln
    
    dp[pos][0] = n
    dp[pos][1] = max + 1

    if totalmax < dp[pos][1]:
      totalmax = dp[pos][1]
  
print(totalmax)

# 얕은 복사로 작동하기 때문이다. 