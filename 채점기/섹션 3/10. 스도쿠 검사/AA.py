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
            
          

# 열검사 

for j in range(9):
    for i in range(9):
        check[mp[i][j]] = 1

    if sum(check) == 10:
        for c in check[1:]:
            c=0
    else:
        print("NO")
        sys.exit(0)


a = [0, 3 ,6]


for i in a:
    for j in a:
        for m in range(3):
            for n in range(3):
                check[mp[i+m][j+n]] = 1

        if sum(check) == 10:
            for c in check[1:]:
                c=0
        else:
            print("NO")
            sys.exit(0)        
    
print("YES")
        