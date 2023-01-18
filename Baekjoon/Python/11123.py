import sys

sys.setrecursionlimit(10**6)


def dfs(i, j):
    grid[i][j] = "."

    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]

        if -1 < nx < h and -1 < ny < w and grid[nx][ny] == "#":
            dfs(nx, ny)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(int(input())):
    h, w = map(int, input().split())

    grid = []
    for _ in range(h):
        grid.append(list(input()))

    cnt = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == "#":
                dfs(i, j)
                cnt += 1

    print(cnt)
