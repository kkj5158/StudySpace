


nstr = input()

intstr = list(map(int, list(nstr)))

intstr.sort(reverse=True) # 내림차순 정렬 2

result = intstr[0]

for num in intstr[1:]:
    if(num == 0 or num == 1):
        result = result+num
    else:
        result = result*num

print(result)