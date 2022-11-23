from collections import deque


def dfs(i, j):
    queue = deque()
    queue.append((i, j))
    cnt = 1

    while queue:
        (y, x) = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (-1 < nx < n and -1 < ny < m):
                continue

            if coor[ny][nx] == 1:
                continue

            coor[ny][nx] = 1
            queue.append((ny, nx))
            cnt += 1

    result.append(cnt)


m, n, k = map(int, input().split())

coor = [[0 for _ in range(n)] for _ in range(m)]

for _ in range(k):
    xs, ys, xe, ye = map(int, input().split())

    for i in range(ys, ye):
        for j in range(xs, xe):
            coor[i][j] = 1

result = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(m):
    for j in range(n):
        if coor[i][j] == 0:
            coor[i][j] = 1
            dfs(i, j)

print(len(result))
print(*sorted(result))
