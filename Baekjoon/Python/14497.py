import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    Q = deque()
    Q.append((x1, y1, 1))
    visited = [[0] * M for _ in range(N)]
    visited[x1][y1] = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while Q:
        x, y, dis = Q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (-1 < nx < N and -1 < ny < M):
                continue

            if visited[nx][ny]:
                continue

            visited[nx][ny] = 1

            if arr[nx][ny] == "#":
                return dis
            elif arr[nx][ny] == "0":
                Q.appendleft((nx, ny, dis))
            else:
                Q.append((nx, ny, dis + 1))


N, M = map(int, input().split())
x1, y1, x2, y2 = map(lambda x: int(x) - 1, input().split())
arr = [list(input().rstrip()) for _ in range(N)]


print(bfs())
