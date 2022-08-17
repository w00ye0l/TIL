from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs():
    while queue:
        (y, x) = queue.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if -1 < ny < n and -1 < nx < m:
                if box[ny][nx] == 0:
                    box[ny][nx] = box[y][x] + 1
                    queue.append((ny, nx))


m, n = map(int, input().split())

box = []
queue = deque()
max_ = 0
sign = True

for i in range(n):
    b = list(map(int, input().split()))
    for j in range(m):
        if b[j] == 1:
            queue.append((i, j))
    box.append(b)

bfs()

for i in box:
    if 0 in i:
        sign = False
    max_ = max(max_, max(i))

if sign == False:
    print(-1)
else:
    print(max_ - 1)
