import sys
sys.stdin=open("10.txt", "rt")

# 맵 구현 

mp = [list(map(int,input().split())) for _ in range(9)]

"""
for x in mp:
    print(x)
"""



# 행 검사 

check = [0]*9
check.insert(0,1)


#print(check)

for x in mp:
    for n in x:
        check[n] = 1
    if sum(check) == 10:
        for c in check[1:]:
            c=0
    else:
        print("No")
        sys.exit(0)
            
          

# 열검사 

for j in range(9):
    for i in range(9):
        check[mp[i][j]] = 1

    if sum(check) == 10:
        for c in check[1:]:
            c=0
    else:
        print("No")
        sys.exit(0)


# 3*3 보드 검사  -> 4중 for 문으로 구현해보기 

# 첫번째 줄 

i,j = 0,0

for i in range




# 두번째 줄 

i,j = 0,3

# 세번째 줄

i,j = 0,6






