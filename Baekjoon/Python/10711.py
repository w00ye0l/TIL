import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    result = 0

    while Q:
        result += 1

        for _ in range(len(Q)):
            x, y = Q.popleft()

            for k in range(8):
                nx = x + dx[k]
                ny = y + dy[k]

                if not (-1 < nx < H and -1 < ny < W):
                    continue

                if graph[nx][ny] != 0:
                    graph[nx][ny] -= 1

                    if graph[nx][ny] == 0:
                        visited[nx][ny] = 1
                        Q.append((nx, ny))

    print(result - 1)


H, W = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(H)]

dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]
visited = [[0] * W for _ in range(H)]
answer = 0
Q = deque()

for i in range(H):
    for j in range(W):
        if graph[i][j] == ".":
            graph[i][j] = 0
            Q.append((i, j))
        else:
            graph[i][j] = int(graph[i][j])

bfs()
