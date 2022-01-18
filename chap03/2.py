n, m, k = map(int , input().split())

data = list(map(int, input().split()))

data.sort()

first = data[n-1]
second = data[n-2]

count = int(m/(k+1))

t = first * k + second

tcount = int(m/k+1)

tnp = int(m&k+1)

total = tcount * t + tnp * first

print(total)



58