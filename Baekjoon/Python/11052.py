n = int(input())

cost = list(map(int, input().split()))

dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(j, i)
        if j % i == 0:
            dp[i][j] = cost[i - 1] * (j // i)
        print(dp)

max_ = 0
for i in range(1, n + 1):
    if max_ < dp[i][-1]:
        max_ = dp[i][-1]

print(max_)
