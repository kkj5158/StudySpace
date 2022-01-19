n, m, k = map(int , input().split())

data = list(map(int, input().split()))

data.sort()

first = data[n-1]
second = data[n-2]

nosecond =int(m/(k+1))
nofirst = m - nosecond

print(nosecond)
print(nofirst)

result = 0

result = first*nofirst + second * nosecond

print(result)