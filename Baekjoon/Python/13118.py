p = list(map(int, input().split()))
x, y, r = map(int, input().split())
result = 0

for i in range(4):
    if x == p[i]:
        result = i + 1

print(result)
