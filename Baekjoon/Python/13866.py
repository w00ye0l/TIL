level = list(map(int, input().split()))
result = 4e4

for i in range(4):
    for j in range(i + 1, 4):
        first = level[i] + level[j]
        second = sum(level) - first

        result = min(result, abs(first - second))

print(result)
