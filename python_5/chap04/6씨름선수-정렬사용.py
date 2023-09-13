import sys
sys.stdin=open("chap04/6.txt", "rt")

n = int(input())

members = []

for _ in range(n):
    members.append(list(map(int,input().split())))


# 키를 기준으로 정렬 
# 
members.sort(key = lambda x: x[0])  

#print(members)

cnt = 0

for i, m in enumerate(members):
    k = m[1]

    for m in members[i+1:]:
        if k < m[1]:
            break
    else:
        cnt+=1
            
    
print(cnt)