import sys
sys.stdin=open("chap03 - 그리디/1.txt", "rt")

n = int(input())

coins = [500, 100, 50, 10] # tuple 공부하기 

count = 0

for coin in coins:
    count = count + n//coin
    n = n % coin
  

print(count)





