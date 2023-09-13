import sys
sys.stdin = open("basic/200자료구조/4.txt")

n = int(input())

ns = []

for _ in range(n):
    ns.append(int(input()))

#print(ns)

st = []

top = 0

for n in ns:
    if(top == n):
        st.pop()
        print('-')
        top -= 1
    else:
        while top<n:
            top += 1
            st.append(top)
            print('+')
        top -= 1    
        st.pop()
        print('-')


