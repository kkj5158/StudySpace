def getnumfrom(str):
    num = ''
    for c in str:
        if c.isdigit():
            num = num + c
    print(num)
    
    num = int(num)

    return num


print(getnumfrom('g0023fg11'))