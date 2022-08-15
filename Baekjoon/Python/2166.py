n = int(input())

x, y = [], []
for i in range(n):
    u, v = map(int, input().split())
    x.append(u)
    y.append(v)

x.append(x[0])
y.append(y[0])

result = 0
for i in range(n):
    result += (x[i] * y[i + 1]) - (x[i + 1] * y[i])

print(abs(result) / 2)
