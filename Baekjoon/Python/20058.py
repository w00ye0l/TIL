import sys
from collections import deque

input = sys.stdin.readline


def firestorm(x, y, l):
    tempGrid = []
    for i in range(y, y + l):
        temp = []

        for j in range(x + l - 1, x - 1, -1):
            temp.append(grid[j][i])

        tempGrid.append(temp)

    for i in range(l):
        for j in range(l):
            grid[x + i][y + j] = tempGrid[i][j]


def melt():
    meltPoint = []

    for i in range(2**n):
        for j in range(2**n):
            cnt = 0

            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]

                if not (-1 < nx < 2**n and -1 < ny < 2**n):
                    continue

                if grid[nx][ny]:
                    cnt += 1

            if cnt < 3:
                meltPoint.append((i, j))

    for m in meltPoint:
        grid[m[0]][m[1]] = max(0, grid[m[0]][m[1]] - 1)


def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = 1
    cnt = 1

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if not (-1 < nx < 2**n and -1 < ny < 2**n):
                continue

            if visited[nx][ny]:
                continue

            if grid[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = 1
                cnt += 1

    return cnt


n, q = map(int, input().split())

grid = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0
visited = [[0] * 2**n for _ in range(2**n)]

for _ in range(2**n):
    grid.append(list(map(int, input().split())))

level = list(map(int, input().split()))

for l in level:
    for i in range(0, 2**n, 2**l):
        for j in range(0, 2**n, 2**l):
            firestorm(i, j, 2**l)

    melt()

for i in range(2**n):
    for j in range(2**n):
        if grid[i][j] > 0 and visited[i][j] == 0:
            answer = max(answer, bfs(i, j))

print(sum(map(sum, grid)))
print(answer)
