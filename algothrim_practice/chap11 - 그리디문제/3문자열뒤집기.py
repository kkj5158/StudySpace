s = input()

sList = list(map(int,list(s)))

cgo = 0
cgz = 0

if sList[0] == 1:
    cgo += 1
else:
    cgz += 1

for i in range(1,len(sList)) :
    if sList[i-1]==0 and sList[i] == 1:
        cgo += 1 
    elif sList[i-1]==1 and sList[i] == 0:
        cgz += 1 

print(min(cgo,cgz))

""" 
if cgo<=cgz:
    print(cgo)
else:
    print(cgz)
 """

