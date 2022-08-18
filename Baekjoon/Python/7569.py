import sys
from collections import deque
input = sys.stdin.readline

dz = [-1, 0, 0, 0, 0, 1]
dy = [0, -1, 1, 0, 0, 0]
dx = [0, 0, 0, -1, 1, 0]


def bfs():
    while queue:
        (z, y, x) = queue.popleft()

        for i in range(6):
            nz = z + dz[i]
            ny = y + dy[i]
            nx = x + dx[i]

            if not (-1 < nz < h):
                continue

            if not (-1 < ny < n):
                continue

            if not (-1 < nx < m):
                continue

            if box[nz][ny][nx] == 0:
                box[nz][ny][nx] = box[z][y][x] + 1
                queue.append((nz, ny, nx))


m, n, h = map(int, input().split())

box = []
queue = deque()
for i in range(h):
    temp2 = []

    for j in range(n):
        temp1 = list(map(int, input().split()))

        for k in range(m):
            if temp1[k] == 1:
                queue.append((i, j, k))

        temp2.append(temp1)

    box.append(temp2)

bfs()

max_ = 0
sign = 1
for i in range(h):
    for j in range(n):
        if 0 in box[i][j]:
            sign = 0
        max_ = max(max_, max(box[i][j]))

if sign == 0:
    print(-1)
else:
    print(max_ - 1)
