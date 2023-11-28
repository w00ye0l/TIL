import sys

input = sys.stdin.readline


def bt(px, py, cnt, t):
    global answer

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    if cnt == K:
        answer = max(answer, t)
        return

    for i in range(px, N):
        for j in range(py if i == px else 0, M):
            if visited[i][j]:
                continue

            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]

                if not (-1 < nx < N and -1 < ny < M):
                    continue

                if visited[nx][ny]:
                    break
            else:
                visited[i][j] = 1
                bt(i, j, cnt + 1, t + graph[i][j])
                visited[i][j] = 0


N, M, K = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
answer = -float("inf")

bt(0, 0, 0, 0)

print(answer)
