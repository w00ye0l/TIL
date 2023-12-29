from collections import deque


def solution(start, end):
    move = [(0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1), (1, 0, 0), (-1, 0, 0)]
    Q = deque()
    Q.append((start, 0))

    while Q:
        (x, y, z), c = Q.popleft()

        for m in move:
            nx = x + m[0]
            ny = y + m[1]
            nz = z + m[2]

            if not (-1 < nx < L and -1 < ny < R and -1 < nz < C):
                continue

            if visited[nx][ny][nz]:
                continue

            if arr[nx][ny][nz] == "." or arr[nx][ny][nz] == "E":
                visited[nx][ny][nz] = c + 1
                Q.append(((nx, ny, nz), c + 1))

    return visited[end[0]][end[1]][end[2]]


while True:
    L, R, C = map(int, input().split())

    if L == 0 and R == 0 and C == 0:
        break

    arr = []
    for i in range(L):
        temp = []
        for j in range(R):
            temp.append(list(input()))

        done = input()
        arr.append(temp)

    for i in range(L):
        for j in range(R):
            for k in range(C):
                if arr[i][j][k] == "S":
                    start = (i, j, k)
                elif arr[i][j][k] == "E":
                    end = (i, j, k)

    visited = [[[0] * C for _ in range(R)] for _ in range(L)]

    answer = solution(start, end)

    if answer:
        print(f"Escaped in {answer} minute(s).")
    else:
        print("Trapped!")
