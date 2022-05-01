import sys
sys.stdin=open("1.txt", "rt")

n = int(input())

words = []

for i in range(n):
    words.append(input())

def isstr(word):
    # 모든 문자를 소문자로 변경한다 
    word = word.lower()

    # 만약 뒤집은 문자열과 기존의 문자열이 동일하면 
    if word[::-1] == word:
        return True
    else:
        return False
    

for i, word in enumerate(words, start=1):
    if isstr(word):
        print("#"+ str(i) +" YES")
    else:
        print("#"+ str(i) +" NO")





