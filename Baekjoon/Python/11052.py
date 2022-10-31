n = int(input())

cost = list(map(int, input().split()))

dp = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], dp[i - j] + cost[j - 1])

print(dp[-1])
