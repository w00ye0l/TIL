import sys

INF = sys.maxsize

n, m = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))
sum_ = sum(cost)
result = INF

dp = [[0 for _ in range(sum_ + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(sum_ + 1):
        if cost[i - 1] <= j:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost[i - 1]] + memory[i - 1])
        else:
            dp[i][j] = dp[i - 1][j]

        if dp[i][j] >= m:
            result = min(result, j)

print(result)
