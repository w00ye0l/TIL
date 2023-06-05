N = int(input())
K = int(input())

dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
answer = 0

for i in range(1, N + 1):
    for j in range(1, K + 1):
        if i / j == 2:
            dp[i][j] = 2
        elif j == 1:
            dp[i][j] = i
        elif dp[i][j] == 0:
            dp[i][j] = dp[i - 1][j] + dp[i - 2][j - 1]

if N / 2 < K:
    print(0)
else:
    print(dp[N][K] % (10**9 + 3))
