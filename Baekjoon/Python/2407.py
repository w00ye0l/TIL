n, m = map(int, input().split())

a = 1
b = 1
for i in range(m):
    a *= n - i
    b *= 1 + i

print(a // b)
