a, b = input().split()

a = list(map(int, a))
b = list(map(int, b))

result = sum(a) * sum(b)

print(result)
