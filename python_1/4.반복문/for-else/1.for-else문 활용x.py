members = [[172, 67], [183, 65], [180, 70], [170, 72], [181, 60]]


cnt = 0
check = 0


for i in range(len(members)):
    h, k = map(int , members[i])
    check = 0
    for m in members:
        if h < m[0] and k < m[1]:
            check = 1
            continue
    if check == 0:
        cnt += 1

print(cnt)

"""
 forelse문을 활용하지 않는 경우는 다음과 같이 check라는 flag를 따로 만들어서
 for문이 모두 돌아가는지 아닌지 판단해야 한다. 
"""