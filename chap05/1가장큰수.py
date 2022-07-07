import sys
sys.stdin=open("chap05/1.txt", "rt")

num, n = map(int, input().split())

num = list(str(num))


# 5 2 7 6 8 2 3 


st = []

st.append(num[0])

for a in num[1:]:

    # 숫자를 교체하지 않는 경우 

    b = st.pop()

    # 숫자를 교체함으로 삭제하는 경우 
    if b <= a and n!=0:
        st.append(a)
        n = n-1
    # 숫자 교체가 필요없는 경우 (기존 숫자가 크다)
    else:
        st.append(b)
        