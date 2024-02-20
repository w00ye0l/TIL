n, m = map(int, input().split())
D = [[1] * m for _ in range(n)]

for i in range(1, n):
    for j in range(1, m):
        D[i][j] = D[i - 1][j - 1] + D[i - 1][j] + D[i][j - 1]

print(D[n - 1][m - 1] % (10**9 + 7))
