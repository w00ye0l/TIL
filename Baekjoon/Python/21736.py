from collections import deque


def bfs():
    global answer
    Q = deque()
    Q.append(doyeon)
    visited = [[0] * M for _ in range(N)]
    visited[doyeon[0]][doyeon[1]] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while Q:
        x, y = Q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (-1 < nx < N and -1 < ny < M):
                continue

            if visited[nx][ny]:
                continue

            if arr[nx][ny] == "P":
                answer += 1
            elif arr[nx][ny] == "X":
                continue

            Q.append((nx, ny))
            visited[nx][ny] = 1


N, M = map(int, input().split())

arr = []
answer = 0

for i in range(N):
    temp = list(input())

    for j in range(M):
        if temp[j] == "I":
            doyeon = (i, j)

    arr.append(temp)

bfs()

if answer == 0:
    print("TT")
else:
    print(answer)
