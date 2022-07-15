import sys
sys.stdin=open("chap05/1.txt", "rt")

num, n = map(int, input().split())

num = list(str(num))

# 5276823 # 7823 

# 딱 3개만 제거가능하도록 -> 1개씩 제거하도록 알고리즘 다시 짜기 

st = []

cnt=0

st.append(num[0])

tmp = num[0]

for a in num[1:]:
    if(n==0):
        st.append(a)
    else:
        if(tmp < a):
            if n==0:
            st.pop()
            n=n-1
            
            st.append(a)
            tmp=a
        else:
            st.append(a)
            st.sort()
            tmp=st[-1]


print(st)


# 해결방법 고민해보기 ! 

# 조건에 대한 정리 