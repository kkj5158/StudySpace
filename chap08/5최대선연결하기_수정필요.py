import sys
sys.stdin=open("chap08/5.txt", "rt")

n = int(input())

nums = list(map(int, input().split()))


# 하나씩 넣는다 . 

# 끝으로 끝났을때 연결된 선의 최대갯수를 dp 에 저장해둔다. 

# 자기보다 작은 값을 탐색하고, 그 중 가장 최대갯수를 가진 값에 + 1 한 값을 dp에 저장한다. 반복한다. 


# 4 1 

# 1 1 

# 2 2
# 
#  

# [num, max]

dp = [[0,0] for _ in range(n+1)]

totalmax = 1

for pos, n in enumerate(nums,1):
  if pos == 1:
    dp[pos][0] = n
    dp[pos][1] = 1
  else :
    max = 0 
    for num, ln in dp[:pos+1]:
      if num < n :
        if max < ln:
          max = ln

    dp[pos][0] = n
    dp[pos][1] = max+1  
     

  if totalmax < dp[pos][1]:
    totalmax = dp[pos][1] 

print(totalmax)


