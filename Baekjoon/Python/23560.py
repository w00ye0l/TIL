n = int(input())

dp = [0 for _ in range(n)]
dp[0] = 2

for i in range(1, n):
    dp[i] = 3 * dp[i - 1]

print(dp[n - 1])
