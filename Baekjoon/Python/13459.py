from collections import deque


def move(x, y, i):
    while True:
        x += dx[i]
        y += dy[i]

        if arr[x][y] == "O":
            return x, y
        if arr[x][y] == "#":
            x -= dx[i]
            y -= dy[i]
            return x, y


def bfs():
    cnt = 1

    while q:
        for _ in range(len(q)):
            rx, ry, bx, by = q.popleft()

            for i in range(4):
                nrx, nry, nbx, nby = rx, ry, bx, by

                nrx, nry = move(nrx, nry, i)
                nbx, nby = move(nbx, nby, i)

                if arr[nbx][nby] == "O":
                    continue

                if arr[nrx][nry] == "O":
                    print(1)
                    return

                if nrx == nbx and nry == nby:
                    if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by):
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]

                if not visited[nrx][nry][nbx][nby]:
                    visited[nrx][nry][nbx][nby] = 1
                    q.append((nrx, nry, nbx, nby))

        cnt += 1

        if cnt > 10:
            print(0)
            return

    print(0)
    return


N, M = map(int, input().split())
arr = []
rx, ry, bx, by = 0, 0, 0, 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(N):
    temp = list(input())

    for j in range(M):
        if temp[j] == "R":
            temp[j] = "."
            rx, ry = i, j
        elif temp[j] == "B":
            temp[j] = "."
            bx, by = i, j

    arr.append(temp)

q = deque()
q.append((rx, ry, bx, by))
visited = [
    [[[0 for _ in range(M)] for _ in range(N)] for _ in range(M)] for _ in range(N)
]
visited[rx][ry][bx][by] = 1

bfs()
