import sys

input = sys.stdin.readline

dp = [[0 for _ in range(4)] for _ in range(100001)]
dp[1][1] = dp[2][2] = dp[3][1] = dp[3][2] = dp[3][3] = 1

for i in range(4, 100001):
    dp[i][1] = (dp[i - 1][2] + dp[i - 1][3]) % 1000000009
    dp[i][2] = (dp[i - 2][1] + dp[i - 2][3]) % 1000000009
    dp[i][3] = (dp[i - 3][1] + dp[i - 3][2]) % 1000000009

for _ in range(int(input())):
    n = int(input())

    print(sum(dp[n]) % 1000000009)
