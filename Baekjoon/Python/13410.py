n, k = map(int, input().split())

result = []

for i in range(1, k + 1):
    result.append(int(str(n * i)[::-1]))

print(max(result))
