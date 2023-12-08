import sys

input = sys.stdin.readline

N = int(input())
graph = [list(input().rstrip()) for _ in range(N)]
answer = [[0] * N for _ in range(N)]

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for i in range(N):
    for j in range(N):
        if graph[i][j] != ".":
            cnt = int(graph[i][j])
            answer[i][j] = "*"

            for k in range(8):
                nx = i + dx[k]
                ny = j + dy[k]

                if not (-1 < nx < N and -1 < ny < N):
                    continue

                if answer[nx][ny] != "M" and answer[nx][ny] != "*":
                    answer[nx][ny] += cnt
                    if answer[nx][ny] >= 10:
                        answer[nx][ny] = "M"

for i in range(N):
    print("".join(map(str, answer[i])))
