import sys
from collections import deque

INF = sys.maxsize

m, n = map(int, input().split())

miro = []
for _ in range(n):
    miro.append(list(map(int, input())))

distance = [[INF for _ in range(m)] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    distance[i][j] = 0

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if not (-1 < nx < n and -1 < ny < m):
                continue

            if distance[nx][ny] > distance[x][y] + miro[nx][ny]:
                distance[nx][ny] = distance[x][y] + miro[nx][ny]
                queue.append((nx, ny))


bfs(0, 0)

print(distance[n - 1][m - 1])
