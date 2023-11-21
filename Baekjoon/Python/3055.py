from collections import deque


def bfs(start):
    Q = deque()
    Q.append(start)
    visited = [[-1] * C for _ in range(R)]
    visited[start[0]][start[1]] = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while Q:
        for _ in range(len(water)):
            x, y = water.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if not (-1 < nx < R and -1 < ny < C):
                    continue

                if graph[nx][ny] == ".":
                    graph[nx][ny] = "*"
                    water.append((nx, ny))

        for _ in range(len(Q)):
            x, y = Q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if not (-1 < nx < R and -1 < ny < C):
                    continue

                if visited[nx][ny] != -1:
                    continue

                if graph[nx][ny] == "." or graph[nx][ny] == "D":
                    visited[nx][ny] = visited[x][y] + 1
                    Q.append((nx, ny))

    return visited


R, C = map(int, input().split())

graph = [list(input()) for _ in range(R)]
water = deque()

for i in range(R):
    for j in range(C):
        if graph[i][j] == "*":
            water.append((i, j))
        elif graph[i][j] == "S":
            start = (i, j)
        elif graph[i][j] == "D":
            end = (i, j)

result = bfs(start)
answer = result[end[0]][end[1]]

if answer == -1:
    print("KAKTUS")
else:
    print(answer)
