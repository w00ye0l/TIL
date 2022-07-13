a, m, d, n = map(int, input().split())
result = a

for i in range(n - 1):
    result = result * m + d

print(result)
