num , n = map(int, input().split())

num = list(map(int, str(num)))

# 5276823 3 

# 

#tos -> -1 


st = []



# 해당 구조에서 do while 문이 사용되지 않아도 되는 이유에 대해서 명확히 이해하고 생각하고 있기. 
for a in num:
    while st and n > 0 and a > st[-1]:
        st.pop()
        n = n-1
    
    st.append(a)

if n !=0 :
    st = st[:-n]


for b in st:
    print(b , end='')

# 5 번 예외 수정하기 

# 5 번 예외 수정하기 



