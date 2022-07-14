import sys
sys.stdin=open("chap05/1.txt", "rt")

num, n = map(int, input().split())

num = list(str(num))

# 5276823 # 7823 

st = []

cnt=0

st.append(num[0])

tmp = num[0]

for a in num[1:]:
    if(n==0):
        st.append(a)
    else:
        if(tmp < a):
            n = n-len(st)
            st.clear()
            st.append(a)
            tmp=a
        else:
            st.append(a)
            st.sort()
            tmp=st[-1]


print(st)


# 해결방법 고민해보기 ! 