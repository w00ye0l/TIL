from collections import deque

n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

visited = [[-1 for _ in range(m)] for _ in range(n)]


def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if not (-1 < nx < n and -1 < ny < m):
                continue

            if visited[nx][ny] != -1:
                continue

            if arr[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1


for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            bfs(i, j)
        elif arr[i][j] == 0:
            visited[i][j] = 0

for i in range(n):
    print(*visited[i])
