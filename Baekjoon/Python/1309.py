MOD_NUM = 9901

n = int(input())

# [[0X], [XO], [XX]]의 경우의 수
dp = [[0, 0, 0] for _ in range(n + 1)]

dp[1] = [1, 1, 1]

for i in range(2, n + 1):
    # i번째 행에 0, 1, 2번 방법의 경우의 수
    dp[i][0] = (dp[i - 1][1] + dp[i - 1][2]) % MOD_NUM
    dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % MOD_NUM
    dp[i][2] = sum(dp[i - 1]) % MOD_NUM

print(sum(dp[n]) % MOD_NUM)
