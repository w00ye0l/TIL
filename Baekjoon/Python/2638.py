from collections import deque

n, m = map(int, input().split())

cheese = []
for _ in range(n):
    cheese.append(list(map(int, input().split())))

queue = deque()

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

cnt = 0
while True:
    if max(map(max, cheese)) == 0:
        break

    visited = [[0 for _ in range(m)] for _ in range(n)]

    queue = deque()
    queue.append((0, 0))
    visited[0][0] = -1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (-1 < nx < n and -1 < ny < m):
                continue

            if visited[nx][ny] == -1:
                continue

            if cheese[nx][ny] == 1:
                visited[nx][ny] += 1
            else:
                queue.append((nx, ny))
                visited[nx][ny] = -1

    for i in range(n):
        for j in range(m):
            if visited[i][j] >= 2:
                cheese[i][j] = 0

    cnt += 1

print(cnt)
