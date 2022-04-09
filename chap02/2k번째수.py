import sys
sys.stdin=open("2.txt", "rt")

t = int(input())



for i in range(t):
    n, s, e, k = map(int, input().split())
    numbers = list(map(int, input().split()))

    slist = numbers[s-1:e]
    slist.sort()

    print("#%d %d" %(i+1, slist[k-1]))

    
    # 배열 인덱스상에서의 0 부터의 시작을 언제나 염두에 두기 -> 항상 배열의 입장에서 접근해야하므로 -1을 해야한다. 