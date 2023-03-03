n = int(input())
p = list(map(int, input().split()))

dp = [p[i - 1] for i in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, i + 1):
        dp[i] = min(dp[i], dp[i - j] + p[j - 1])

print(dp[n])
