H, Y = map(int, input().split())

dp = [H] * (Y + 1)

for i in range(1, Y + 1):
    if i >= 5:
        dp[i] = max(dp[i], int(dp[i - 5] * (1.35)))
    if i >= 3:
        dp[i] = max(dp[i], int(dp[i - 3] * (1.2)))

    dp[i] = max(dp[i], int(dp[i - 1] * (1.05)))

print(dp[-1])
