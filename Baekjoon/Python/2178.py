from collections import deque


def bfs(i, j):
    now = deque()
    now.append((i, j))
    while now:
        i, j = now.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            if 0 <= ni < n and 0 <= nj < m:
                if maze[ni][nj] == 1:
                    maze[ni][nj] = maze[i][j] + 1
                    now.append((ni, nj))
    return maze[n - 1][m - 1]


di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

n, m = map(int, input().split())
maze = []
for _ in range(n):
    maze.append(list(map(int, input())))

print(bfs(0, 0))
