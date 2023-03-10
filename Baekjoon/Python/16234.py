from collections import deque


def bfs(i, j, idx):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = idx
    node = []
    node.append((i, j))
    people = area[i][j]
    cnt = 1

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if not (-1 < nx < n and -1 < ny < n):
                continue

            if visited[nx][ny] != 0:
                continue

            if not (l <= abs(area[x][y] - area[nx][ny]) <= r):
                continue

            queue.append((nx, ny))
            node.append((nx, ny))
            people += area[nx][ny]
            cnt += 1
            visited[nx][ny] = idx

    for u, v in node:
        temp[u][v] = int(people / cnt)


n, l, r = map(int, input().split())
area = []
result = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
    area.append(list(map(int, input().split())))

while True:
    visited = [[0 for _ in range(n)] for _ in range(n)]
    temp = [[0 for _ in range(n)] for _ in range(n)]
    idx = 0

    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                idx += 1
                bfs(i, j, idx)

    area = [temp[i][:] for i in range(n)]

    if idx == n**2:
        break

    result += 1

print(result)
