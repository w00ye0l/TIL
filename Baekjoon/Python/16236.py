from collections import deque


def bfs(i, j, lv, cnt, t):
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    queue = deque()
    queue.append((i, j))
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    visited[i][j] = 0
    graph[i][j] = 0
    can = []

    while queue:
        (x, y) = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (-1 < nx < n and -1 < ny < n):
                continue

            if visited[nx][ny] == -1:
                if graph[nx][ny] == 0 or graph[nx][ny] == lv:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))

                if 0 < graph[nx][ny] < lv:
                    visited[nx][ny] = visited[x][y] + 1
                    can.append([nx, ny, visited[nx][ny]])

    if can:
        can = sorted(can, key=lambda x: (x[2], x[0], x[1]))
        graph[can[0][0]][can[0][1]] = 9

        cnt += 1
        if cnt == lv:
            lv += 1
            cnt = 0

        t += can[0][2]

        return bfs(can[0][0], can[0][1], lv, cnt, t)
    else:
        return t


n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

lv = 2
cnt = 0
t = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            print(bfs(i, j, lv, cnt, t))
