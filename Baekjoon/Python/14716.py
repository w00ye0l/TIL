import sys

sys.setrecursionlimit(10**6)

m, n = map(int, input().split())

arr = []

for _ in range(m):
    arr.append(list(map(int, input().split())))


def dfs(x, y):
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    for k in range(8):
        nx = x + dx[k]
        ny = y + dy[k]

        if not (-1 < nx < m and -1 < ny < n):
            continue

        if arr[nx][ny] == 1:
            arr[nx][ny] = 0
            dfs(nx, ny)


cnt = 0
for i in range(m):
    for j in range(n):
        if arr[i][j] == 1:
            dfs(i, j)
            cnt += 1

print(cnt)
