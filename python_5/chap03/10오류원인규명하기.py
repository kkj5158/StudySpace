import sys
sys.stdin=open("chap03/10.txt", "rt")

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
        print("NO")
        sys.exit(0)
            
          