n, k = map(int, input().split())

dp = [[0 for _ in range(n + 1)] for _ in range(k)]

for i in range(k):
    for j in range(n + 1):
        for l in range(j + 1):
            if i == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = (dp[i - 1][j - l] + dp[i][j]) % 1000000000

print(dp[k - 1][n])
