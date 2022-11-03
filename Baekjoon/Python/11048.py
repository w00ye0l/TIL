n, m = map(int, input().split())

maze = []

for _ in range(n):
    maze.append(list(map(int, input().split())))

dp = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if j == 0:
            if i == 0:
                dp[i][j] = maze[i][j]
            else:
                dp[i][j] = dp[i - 1][j] + maze[i][j]

        elif i == 0:
            if j == 0:
                dp[i][j] = maze[i][j]
            else:
                dp[i][j] = dp[i][j - 1] + maze[i][j]
        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + maze[i][j]

print(dp[n - 1][m - 1])
