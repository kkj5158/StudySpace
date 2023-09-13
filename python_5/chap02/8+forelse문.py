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