from collections import deque

t = int(input())

for _ in range(t):
    l = int(input())
    y, x = map(int, input().split())
    wy, wx = map(int, input().split())

    dy = [-2, -1, 1, 2, 2, 1, -1, -2]
    dx = [1, 2, 2, 1, -1, -2, -2, -1]

    visited = [[0] * l for _ in range(l)]
    queue = deque()
    queue.append((y, x))

    while queue:
        y, x = queue.popleft()

        if y == wy and x == wx:
            break

        for k in range(8):
            ny = y + dy[k]
            nx = x + dx[k]

            if not (-1 < ny < l and -1 < nx < l):
                continue

            if visited[ny][nx] == 0:
                visited[ny][nx] = visited[y][x] + 1
                queue.append((ny, nx))

    print(visited[wy][wx])
