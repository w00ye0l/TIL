from collections import deque


def bfs(i, j, team):
    queue = deque()
    cnt = 1
    queue.append((i, j))
    visited[i][j] = cnt

    while queue:
        (x, y) = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if not (-1 < nx < m and -1 < ny < n):
                continue

            if visited[nx][ny]:
                continue

            if soldier[nx][ny] == team:
                cnt += 1
                visited[nx][ny] = 1
                queue.append((nx, ny))

    if team == 'W':
        result[0] += cnt ** 2
    else:
        result[1] += cnt ** 2


n, m = map(int, input().split())

soldier = []
for _ in range(m):
    temp = list(input())

    soldier.append(temp)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = [0, 0]

visited = [[0 for _ in range(n)] for _ in range(m)]

for i in range(m):
    for j in range(n):
        if soldier[i][j] == 'W' and visited[i][j] == 0:
            bfs(i, j, 'W')

        elif soldier[i][j] == 'B' and visited[i][j] == 0:
            bfs(i, j, 'B')


print(*result)
