from collections import deque

n, m = map(int, input().split())

coor = []
for _ in range(n):
    temp = list(map(int, input()))

    coor.append(temp)

visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    queue = deque()

    queue.append((0, 0, 0))
    visited[0][0][0] = 1

    while queue:
        x, y, z = queue.popleft()

        if x == n - 1 and y == m - 1:
            return visited[x][y][z]

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if not (-1 < nx < n and -1 < ny < m):
                continue

            if coor[nx][ny] == 0 and visited[nx][ny][z] == 0:
                visited[nx][ny][z] = visited[x][y][z] + 1
                queue.append((nx, ny, z))

            elif coor[nx][ny] == 1 and z == 0:
                visited[nx][ny][z + 1] = visited[x][y][z] + 1
                queue.append((nx, ny, z + 1))

    return -1


print(bfs())
