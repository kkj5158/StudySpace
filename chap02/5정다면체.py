import sys
sys.stdin=open("5.txt", "rt")

# list 사용하여서 그리디 적용 이중 for문 사용해서 모든 경우의 수, list에 넣기, 각각의 갯수를 구하고 가장 높은 확률 구하기

n, m = map(int, input().split())

nlist = []
mlist = []

tlist = []
slist = []

for i in range(1, n+1):
    nlist.append(i)

for i in  range(1, m+1):
    mlist.append(i)

for n in nlist:
    for m in mlist:
        tlist.append(n+m)


max = 1

for i in range(2, n+m):
    if tlist.count(i)>=max:
        max = tlist.count(i)

for i in range(2, n+m):
    if tlist.count(i) == max:
        slist.append(i)

print(*slist, sep=' ')

# 리스트 언팩 -> https://www.delftstack.com/ko/howto/python/list-without-brackets-python/#str%25ED%2595%25A8%25EC%2588%2598%25EB%25A5%25BC-%25EC%2582%25AC%25EC%259A%25A9%25ED%2595%2598%25EC%2597%25AC-%25EB%258C%2580%25EA%25B4%2584%25ED%2598%25B8%25EC%2597%2586%25EC%259D%25B4-%25EB%25AA%25A9%25EB%25A1%259D-%25EC%259D%25B8%25EC%2587%2584

        