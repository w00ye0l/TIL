from pprint import pprint
from collections import deque


def bomb(x, y):
    global cnt

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [(x, y)]
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (-1 < nx < 12 and -1 < ny < 6):
                continue

            if (nx, ny) in visited:
                continue

            if temp[nx][ny] == temp[x][y]:
                visited.append((nx, ny))
                queue.append((nx, ny))

    if len(visited) >= 4:
        cnt += 1
        for v in visited:
            temp[v[0]][v[1]] = "_"


def move():
    for i in range(12):
        for j in range(6):
            if temp[i][j] == "_":
                for k in range(i, -1, -1):
                    if k == 0:
                        temp[k][j] = "."
                    else:
                        temp[k][j] = temp[k - 1][j]
                # pprint(field)


field = [list(input()) for _ in range(12)]

# print(field)
answer = 0

while True:
    cnt = 0
    temp = field[:]

    for i in range(11, -1, -1):
        for j in range(6):
            if temp[i][j] != ".":
                bomb(i, j)

    if cnt == 0:
        break
    else:
        answer += 1

    move()

print(answer)
