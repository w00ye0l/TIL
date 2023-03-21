import sys

INF = sys.maxsize

n = int(input())

matrix = []

for _ in range(n):
    matrix.append(tuple(map(int, input().split())))

dp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n - 1):
    for j in range(n - i - 1):
        dp[j][i + j + 1] = INF

        for k in range(j, i + j + 1):
            print(i, j, k)
            dp[j][i + j + 1] = min(
                dp[j][i + j + 1],
                dp[j][k]
                + dp[k + 1][i + j + 1]
                + matrix[j][0] * matrix[i + j + 1][1] * matrix[k][1],
            )

print(dp[0][-1])
