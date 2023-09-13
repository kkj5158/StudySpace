

numbers = list(map(int, list(input())))

front=numbers[0 : len(numbers)//2]
rear=numbers[len(numbers)//2 : len(numbers)]

sumf=0
sumr=0

for n in front :
    sumf += n

for n in rear:
    sumr += n

if(sumf==sumr):
    print("LUCKY")
else:
    print("READY")


