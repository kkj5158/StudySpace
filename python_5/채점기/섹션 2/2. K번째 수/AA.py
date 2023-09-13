#import sys
#sys.stdin=open("2.txt", "rt")

t = int(input())



for i in range(t):
    n, s, e, k = map(int, input().split())
    numbers = list(map(int, input().split()))

    slist = numbers[s-1:e]
    slist.sort()

    print("#%d %d" %(i+1, slist[k-1]))
