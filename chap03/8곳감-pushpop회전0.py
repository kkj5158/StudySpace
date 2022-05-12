import sys
sys.stdin=open("8.txt", "rt")

n = int(input())

mp = []

mp.append([0]*n)

for _ in range(n):
    mp.append(list(map(int, input().split()))) # 1행부터 시작 고려하기 

#print(mp)

m = int(input())

#print(m)

moves = [list(map(int, input().split())) for _ in range(m)]

#print(moves)



# moves 실행하기 

for move in moves:
    row , dir , num = map(lambda x:x, move) # map 의 언팩킹 기능 사용 # x는 단순히 x로 변환한다. 
    #print(row, dir, num)

    # 방향이 왼쪽인경우 
    if dir == 0 :
        for i in range(n):
            str = mp[row].pop(0)
            mp[row].append(str)
    # 방향이 오른쪽인경우 
    else :
        for i in range(n):
            str = mp[row].pop()
            mp[row].append(str)
             

        

# 감 갯수 구하기 

mid = n//2

l = 0
r = n

total = 0 

for m in mp:
    total += sum(m[l:r])
    if n < mid:
        l += 1
        r -= 1
    else:
        l -= 1
        r += 1

print(total)


