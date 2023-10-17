import sys
from collections import deque

input = sys.stdin.readline


def bfs(i, j):
    Q = deque()
    Q.append((i, j, 0))
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[i][j] = 1
    dis[i][j] = 0

    while Q:
        x, y, d = Q.popleft()

        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]

            if not (-1 < nx < n and -1 < ny < m):
                continue

            if visited[nx][ny]:
                continue

            if arr[nx][ny] == 0:
                Q.append((nx, ny, d + 1))
                dis[nx][ny] = min(dis[nx][ny], d + 1)
                visited[nx][ny] = 1


n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
dis = [[float("inf") for _ in range(m)] for _ in range(n)]

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            bfs(i, j)

print(max(map(max, dis)))
