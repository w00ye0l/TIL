N, M = map(int, input().split())

a, b = 100 - N, 100 - M
c = 100 - (a + b)
d = a * b
q = d // 100
r = d % 100

print(a, b, c, d, q, r)
print(c + q, r)
