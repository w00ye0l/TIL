from heapq import heappush, heappop


def dijkstra():
    Q = []
    heappush(Q, (0, (0, 0)))
    visited = [[float("inf")] * 501 for _ in range(501)]
    visited[0][0] = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while Q:
        dis, (x, y) = heappop(Q)

        if x == 500 and y == 500:
            return visited[-1][-1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (-1 < nx < 501 and -1 < ny < 501):
                continue

            if graph[nx][ny] == 2:
                continue

            if visited[nx][ny] == float("inf"):
                visited[nx][ny] = min(visited[nx][ny], visited[x][y] + graph[nx][ny])
                heappush(Q, (visited[nx][ny], (nx, ny)))

    return -1


graph = [[0] * 501 for _ in range(501)]

N = int(input())
for _ in range(N):
    X1, Y1, X2, Y2 = map(int, input().split())

    for i in range(min(X1, X2), max(X1, X2) + 1):
        for j in range(min(Y1, Y2), max(Y1, Y2) + 1):
            graph[i][j] = 1

M = int(input())
for _ in range(M):
    X1, Y1, X2, Y2 = map(int, input().split())

    for i in range(min(X1, X2), max(X1, X2) + 1):
        for j in range(min(Y1, Y2), max(Y1, Y2) + 1):
            graph[i][j] = 2

graph[0][0] = 0

print(dijkstra())
