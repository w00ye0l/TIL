from collections import defaultdict

n = int(input())

num = list(map(int, input().split()))

dp = [defaultdict(int) for _ in range(n - 1)]


def check(idx):
    for k, v in dp[idx - 1].items():
        if 0 <= k + num[idx] <= 20:
            dp[idx][k + num[idx]] += v

        if 0 <= k - num[idx] <= 20:
            dp[idx][k - num[idx]] += v


dp[0][num[0]] = 1

for i in range(1, n - 1):
    check(i)

print(dp[n - 2][num[-1]])
