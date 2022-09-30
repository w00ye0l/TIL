from collections import deque


def bfs1(i, j, color, cnt):
    queue = deque()
    queue.append((i, j))
    visited1[i][j] = cnt

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        (x, y) = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if not (-1 < nx < n and -1 < ny < n):
                continue

            if visited1[nx][ny]:
                continue

            if color == "R" or color == "G":
                if rgb[nx][ny] in ["R", "G"]:
                    visited1[nx][ny] = cnt
                    queue.append((nx, ny))
            else:
                if rgb[nx][ny] == color:
                    visited1[nx][ny] = cnt
                    queue.append((nx, ny))


def bfs2(i, j, color, cnt):
    queue = deque()
    queue.append((i, j))
    visited2[i][j] = cnt

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        (x, y) = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if not (-1 < nx < n and -1 < ny < n):
                continue

            if visited2[nx][ny]:
                continue

            if rgb[nx][ny] == color:
                visited2[nx][ny] = cnt
                queue.append((nx, ny))


n = int(input())

rgb = []
for _ in range(n):
    rgb.append(list(input()))

visited1 = [[0 for _ in range(n)] for _ in range(n)]
visited2 = [[0 for _ in range(n)] for _ in range(n)]

cnt1 = 0
cnt2 = 0
for i in range(n):
    for j in range(n):
        if visited1[i][j] == 0:
            cnt1 += 1
            bfs1(i, j, rgb[i][j], cnt1)
        if visited2[i][j] == 0:
            cnt2 += 1
            bfs2(i, j, rgb[i][j], cnt2)

print(cnt2, cnt1)
