n = int(input())

building = list(map(int, input().split()))
result = []

for i in range(n):
    lt, rt = 1e10, -1e10
    cnt = 0
    for j in range(i - 1, -1, -1):
        if lt > (building[i] - building[j]) / (i - j):
            lt = (building[i] - building[j]) / (i - j)
            cnt += 1

    for k in range(i + 1, n):
        if rt < (building[k] - building[i]) / (k - i):
            rt = (building[k] - building[i]) / (k - i)
            cnt += 1

    result.append(cnt)

print(max(result))
