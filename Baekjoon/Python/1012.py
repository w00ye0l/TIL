import sys
sys.setrecursionlimit(10 ** 6)

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def dfs(i, j, m, n, farms):
    if farms[i][j] == 1:
        farms[i][j] = 0

        for k in range(4):
            ny = i + dy[k]
            nx = j + dx[k]

            if not (-1 < ny < n and -1 < nx < m):
                continue

            if farms[ny][nx] == 0:
                continue

            dfs(ny, nx, m, n, farms)

    return 1


t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())

    farms = [[0] * m for _ in range(n)]
    worm = 0

    for _ in range(k):
        u, v = map(int, input().split())
        farms[v][u] = 1

    for i in range(n):
        for j in range(m):
            if farms[i][j] == 1:
                worm += dfs(i, j, m, n, farms)

    print(worm)
