import sys
sys.stdin=open("chap05/1.txt", "rt")

num , n = map(int, input().split())

arr = list(str(num))

st = []

# 컴퓨터가 이해할 수 있는 가장 단순하면서도 컴퓨터적인 해결방법을 탐색한다. 
# 가장 간단한 규칙을 만들어줘야 한다. 
# 스택이라는 도구를 가져다 쓴다. 스택은 특정원소를 추가하고 빼내는데 가장 좋은 자료구조이다. 

# 스택이라는 해결도구에 집중해보자. 

top = arr[0]


for a in arr:
  if top>=a:
    st.append(a)
    top = st[-1]
  else:
    while n>0 and top<a and len(st)>0:
      st.pop()
      if len(st)>0:
        top = st[-1]
      n=n-1
    
    st.append(a)
    top=st[-1]

while n>0:
  st.pop()
  n=n-1



print(*st ,sep='')


    

    

  


