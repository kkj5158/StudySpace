arr = [5, 3, 7, 9, 2, 5, 2 , 6]

arrMin=float('inf') # 가장 큰수 

for a in arr:
    if a<arrMin:
        arrMin = a

print(arrMin)
