p, q = map(int, input().split())

result = 0

for i in range(p):
    data = list(map(int, input().split))
    min_value = 10001
    for a in range(data):
        min_value = min(a, min_value)

    result = max(result, min_value)

print(result)
    