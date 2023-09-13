# 딕셔너리 생성 
d = {'a': 123123}

# 값 추가 
d[999] = 10 # 숫자 키, 숫자 값
d['99'] = 111 # 문자 키, 숫자 값 
d['blodckDmask'] = "blog" # 문자 키, 문자 값 
d['wow'] = [1, 2, 3, 4, 5] # 문자 키 , 리스트 값 
d[(1,2)] = "this is value" # 튜플 키, 튜플 값 
d[1] = (3, 'a', 5) # 숫자 키, 튜플 값 

# 값 접근
print(d[999])
print(d['blodckDmask'])

#값 변경
print(d[999])
d[999] = 11
print(d[999])

# 빈딕셔너리 생성
dict1 = {} # {}
dict2 = dict() # {}
# 특정 key-value쌍을 가진 dictionary 선언

Dog = {
    'name': '동동이',
    'weight': 4,
    'height': 100,
}


'''
{'height': 100, 'name': '동동이', 'weight': 4}
'''
# dictionary를 value로 가지는 dictionary 선언

Animals = {
    'Dog': {
        'name': '동동이',
        'age': '5'
    },
    'Cat': {
        'name': '야옹이',
        'weight': 3
    }
}


'''
 { 'Dog': { 'name': '동동이', 'age': '5'},
   'Cat': {'name': '야옹이','weight': 3 }}
'''