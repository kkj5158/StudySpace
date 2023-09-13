import sys
sys.stdin=open("chap03 - 그리디/1.txt", "rt")

n = int(input())
count = 0


coin_types = [500 , 100, 50 , 10]


for coin in coin_types:
    count += n//coin
    n %= coin

print(count)



# typeerror check 하기 