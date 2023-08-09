N, M = map(int, input().split())

dp = [1 for _ in range(M)]

for i in range(M, N + 1):
    dp.append((dp[i - 1] + dp[i - M]) % (10**9 + 7))

print(dp[N])
