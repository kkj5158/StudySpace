

n = int(input("금액을 입력하세요 "))

coins = [500, 100, 50, 10] # tuple 공부하기 

count = 0

for coin in coins:
    count = count + n//coin
    n = n % coin
  

print(count)





