n, s, m = map(int, input().split())
v = list(map(int, input().split()))
dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
dp[0][s] = 1
result = -1

for i in range(n):
    for j in range(m + 1):
        if dp[i][j] == 1:
            if j + v[i] <= m:
                dp[i + 1][j + v[i]] = 1
            if j - v[i] >= 0:
                dp[i + 1][j - v[i]] = 1

for i in range(m, -1, -1):
    if dp[n][i] == 1:
        result = i
        break

print(result)
