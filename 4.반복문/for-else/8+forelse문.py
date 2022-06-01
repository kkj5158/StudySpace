def isPrime(x):
    if x == 1 :
        return 0
    elif x == 2:
        return 1
    else:
        for i in range(2, x):
            if x%i == 0:
                return False # 소수가 아니다 .
        else:
            return True # 소수이다. 

# for-else 문 : break나 return 문이 걸리지 않고 모든 for문이 돌아갔을때 발동 