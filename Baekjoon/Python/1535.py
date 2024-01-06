N = int(input())
health = [0] + list(map(int, input().split()))
happiness = [0] + list(map(int, input().split()))

dp = [[0] * (100) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, 100):
        if health[i] <= j:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - health[i]] + happiness[i])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[N][-1])
