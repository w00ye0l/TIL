N, M = map(int, input().split())
dp = [[0] * (M + 1)]
for _ in range(N):
    dp.append([0] + list(map(int, input().split())))

for i in range(1, N + 1):
    for j in range(1, M + 1):
        dp[i][j] = dp[i][j] + max(dp[i - 1][j], dp[i][j - 1])

print(dp[N][M])
