cost = list(map(int, input().split()))
park = [0 for _ in range(101)]
max_end = 0
result = 0

for i in range(3):
    start, end = map(int, input().split())

    for j in range(start, end):
        park[j] += 1

    if end > max_end:
        max_end = end

for i in range(1, max_end):
    result += park[i] * cost[park[i] - 1]

print(result)
