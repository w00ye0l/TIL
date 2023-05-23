n, k = map(int, input().split())
coin_li = sorted([int(input()) for _ in range(n)])
dp = [10001] * (k + 1)
dp[0] = 0
for i in range(1, k + 1):
    for c in coin_li:
        if i - c < 0:
            break
        else:
            dp[i] = min(dp[i - c] + 1, dp[i])
print(-1 if dp[k] == 10001 else dp[k])
