from collections import deque
from itertools import combinations


def bfs(arr):
    # 벽은 미리 -2로 초기화 방문하지 않은 곳은 -1로 초기화
    visited = [[-2 if graph[j][i] == 1 else -1 for i in range(N)] for j in range(N)]

    # 바이러스의 시작점들은 0으로 미리 초기화
    for a in arr:
        visited[a[0]][a[1]] = 0

    while arr:
        x, y, t = arr.popleft()
        visited[x][y] = t

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (-1 < nx < N and -1 < ny < N):
                continue

            if visited[nx][ny] != -1:
                continue

            if graph[nx][ny] != 1:
                visited[nx][ny] = t + 1
                arr.append((nx, ny, t + 1))

    return visited


def calResult(visited):
    result = -1
    zeroCnt = 0

    # 벽이 아닌 곳에서 방문 안한 곳이 있는지 체크
    for v in visited:
        if -1 in v:
            return -1

        zeroCnt += v.count(0)

    # 0는 바이러스의 시작점이므로 M과 같은지 체크
    if zeroCnt == M:
        result = max(map(max, visited))

    return result


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
answer = float("inf")
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
canVirus = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            canVirus.append((i, j, 0))

for c in combinations(canVirus, M):
    result = calResult(bfs(deque(c)))

    if result != -1:
        answer = min(answer, result)

print(answer) if answer != float("inf") else print(-1)
