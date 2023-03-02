n, t = map(int, input().split())

dp = [[0 for _ in range(t + 1)] for _ in range(n + 1)]
k_list, s_list = [], []

for _ in range(n):
    k, s = map(int, input().split())
    k_list.append(k)
    s_list.append(s)

for i in range(n + 1):
    for j in range(t + 1):
        if i == 0 or j == 0:
            dp[i][j] = 0

        elif k_list[i - 1] <= j:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - k_list[i - 1]] + s_list[i - 1])

        else:
            dp[i][j] = dp[i - 1][j]

print(dp[n][t])
