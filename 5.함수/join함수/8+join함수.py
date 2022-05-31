# https://blockdmask.tistory.com/468


# 1 리스트를 문자열로 

from cmath import pi


a = ['a', 'b', 'c', 'd', '1', '2', '3']


print(a)

a = ''.join(a)

print(a)

a = '_'.join(a)

print(a)

a='**'.join(a)

print(a)

# 2 리스트를 문자열로 합치기 

a = ['BlockDMask', 'python', 'join', 'example']

print(a)
print()

result1 = "_".join(a)

result2 = ".".join(a)

print(result1)

print(result2)

# 3 리스트를 문자열로 합치기 ( 온점과 개행  )


a = ['BlockDMask', 'python', 'join', 'example']

print(a)

result = ".\n".join(a)

print(result)

