import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
max_temp = max(map(max, graph))
max_ = 0


def dfs(i, j, sum_, cnt):
    global max_

    if sum_ + (max_temp * (4 - cnt)) <= max_:
        return

    if cnt == 4:
        max_ = max(max_, sum_)
        return

    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]

        if not (-1 < nx < n and -1 < ny < m):
            continue

        if visited[nx][ny]:
            continue

        if cnt == 2:
            visited[nx][ny] = 1
            dfs(i, j, sum_ + graph[nx][ny], cnt + 1)
            visited[nx][ny] = 0

        visited[nx][ny] = 1
        dfs(nx, ny, sum_ + graph[nx][ny], cnt + 1)
        visited[nx][ny] = 0


for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i, j, graph[i][j], 1)
        visited[i][j] = 0

print(max_)
