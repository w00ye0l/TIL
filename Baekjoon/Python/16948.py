from collections import deque


def bfs(r1, c1):
    Q = deque()
    Q.append((r1, c1))

    while Q:
        x, y = Q.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (-1 < nx < N and -1 < ny < N):
                continue

            if visited[nx][ny] == -1:
                Q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1


N = int(input())

r1, c1, r2, c2 = map(int, input().split())

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

visited = [[-1 for _ in range(N)] for _ in range(N)]
visited[r1][c1] = 0

bfs(r1, c1)

print(visited[r2][c2])
