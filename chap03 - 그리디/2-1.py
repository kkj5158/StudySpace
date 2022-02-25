n, m , k = map(int, input().split())

index = list(map(int, input().split()))

index.sort()

first = index[n-1]
second = index[n-2]

token = first*m + second
numt = m/k
numreg = m - numt

result = numt*token + numreg*first

print(result)