import sys
sys.stdin = open("basic/200자료구조/1.txt")


sn=next(sys.stdin)

# ?? next는 뭐지 

print(sys.stdin)

for line in sn:
    print(line)



# 참고 : https://dojang.io/mod/page/view.php?id=2408
# 참고 2 : https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline