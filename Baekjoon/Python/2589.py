from collections import deque


def bfs(x, y):
    t = 0
    queue = deque()
    queue.append((x, y))
    visited[x][y] = t

    while queue:
        x, y = queue.popleft()
        t = visited[x][y]

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if not (-1 < nx < n and -1 < ny < m):
                continue

            if visited[nx][ny] != -1:
                continue

            if area[nx][ny] == "L":
                queue.append((nx, ny))
                visited[nx][ny] = t + 1

    return t


n, m = map(int, input().split())

area = []

for _ in range(n):
    area.append(list(input()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 0

for i in range(n):
    for j in range(m):
        if not (i == 0 or i == n - 1):
            if area[i - 1][j] == "L" and area[i + 1][j] == "L":
                continue

        if not (j == 0 or j == m - 1):
            if area[i][j - 1] == "L" and area[i][j + 1] == "L":
                continue

        if area[i][j] == "L":
            visited = [[-1 for _ in range(m)] for _ in range(n)]
            result = max(result, bfs(i, j))

print(result)
