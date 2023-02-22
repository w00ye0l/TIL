n = int(input())

edge = []
b = 0

for _ in range(n):
    u, v = map(int, input().split())
    b = max(b, v)
    edge.append((u, v))

dp = [1 for _ in range(b + 1)]

edge.sort()

for i in range(n):
    for j in range(i - 1, -1, -1):
        if edge[i][1] > edge[j][1]:
            dp[i] = max(dp[j] + 1, dp[i])

print(n - max(dp))
