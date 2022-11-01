n, k = map(int, input().split())

coin = []

for _ in range(n):
    coin.append(int(input()))

dp = [0 for _ in range(k + 1)]
dp[0] = 1

for i in range(n):
    for j in range(coin[i], k + 1):
        dp[j] = dp[j] + dp[j - coin[i]]

print(dp[-1])
