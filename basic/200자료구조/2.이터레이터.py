it = iter(range(3))

print(next(it))

print(next(it))

print(next(it))


print("리스트의 이터레이터 화 ")


a = [0, 1, 2, 3, 4, 5, 6]

a = iter(a)

print(next(a))

print(next(a))

print(next(a))

print(next(a))

print(next(a))

# iterator의 값을 가져오는 가장 일반적인 방법은 다음과 같이 for문을 활용하는 것이다. 

a = [1, 2, 3]

ia = iter(a)

for i in ia:
    print(i)


# for 문 안에는 netx가 자동으로 실행된다.  



#print(next(a))

# 리스트 오브젝트는 이터레이터가 아니다. 

# 이터레이터는 무엇인가 ? 

# 이터레이터블과 이터레이터의 차이점은 무엇인가 ? 

# 