p = []

for _ in range(3):
    x, y = map(int, input().split())
    p.append([x, y])

p.append(p[0])

a, b = 0, 0
for i in range(3):
    a += p[i][0] * p[i + 1][1]
    b += p[i][1] * p[i + 1][0]

if a - b > 1:
    print(1)
elif a - b == 0:
    print(0)
else:
    print(-1)
