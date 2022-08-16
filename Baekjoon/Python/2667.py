from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(i, j, n, maps):
    queue = deque()
    cnt = 0
    queue.append((i, j))

    while queue:
        y, x = queue.popleft()
        if maps[y][x] == 1:
            maps[y][x] = 0
            cnt += 1

            for k in range(4):
                ny = y + dy[k]
                nx = x + dx[k]

                if not (-1 < ny < n and -1 < nx < n):
                    continue

                if maps[ny][nx] == 1:
                    queue.append((ny, nx))

    return cnt


n = int(input())

maps = []
visited = [[0] * n for _ in range(n)]
for _ in range(n):
    maps.append(list(map(int, input())))

house = []
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            house.append(bfs(i, j, n, maps))

print(len(house))
house.sort()
for h in house:
    print(h)
