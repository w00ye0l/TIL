n = int(input())

miro = []

for i in range(n):
    miro.append(list(map(int, input().split())))

dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if miro[i][j] == 0:
            continue

        x = i + miro[i][j]
        y = j + miro[i][j]

        if x < n:
            dp[x][j] += dp[i][j]

        if y < n:
            dp[i][y] += dp[i][j]

print(dp[n - 1][n - 1])
