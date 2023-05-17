dp = [0] * 5001
dp[0], dp[2] = 1, 1

for i in range(4, 5001, 2):
    for j in range(2, i + 1, 2):
        dp[i] += dp[j - 2] * dp[i - j] % 1000000007

T = int(input())

for _ in range(T):
    L = int(input())

    print(dp[L] % 1000000007)
