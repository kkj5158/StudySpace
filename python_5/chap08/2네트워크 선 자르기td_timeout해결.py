import sys
sys.stdin=open("chap08/2.txt", "rt")


def d(v):
  if v == 1:
    result = 1;
  elif v == 2:
    result = 2;
  else:
    result = d(v-1) + d(v-2)

  return result


n = int(input())

result = 0

print(d(n))

# 탑다운 방식이면은 재귀로 쪼개나간다 . 
# dp가 바텀업이면 재귀는 탑다운이다. 
# 점화식 생각하기 

# d(1) = 1 
# d(2) = 2
# d(3) = 3  
# d(4) = 

# 1 1 1 1 

# 1 2 1

# 2 1 1

 

# d(v) = d(v-2) + d(v-1)  ( 3 이상부터 )