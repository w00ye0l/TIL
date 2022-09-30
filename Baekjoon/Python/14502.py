from itertools import combinations
from collections import deque
from copy import deepcopy


def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[i][j] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        (x, y) = queue.popleft()
        visited[x][y] = 1

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if not (-1 < nx < n and -1 < ny < m):
                continue

            if visited[nx][ny]:
                continue

            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                queue.append((nx, ny))


n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

wall = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            wall.append((i, j))

build_wall = list(set(combinations(wall, 3)))
result = []

for b in build_wall:
    temp = deepcopy(graph)

    for num in b:
        temp[num[0]][num[1]] = 1

    for i in range(n):
        for j in range(m):
            if temp[i][j] == 2:
                bfs(i, j)

    sum_ = 0
    for t in temp:
        sum_ += t.count(0)

    result.append(sum_)

print(max(result))
