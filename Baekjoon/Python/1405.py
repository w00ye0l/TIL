def dfs(x, y, cnt, p):
    global answer

    if cnt == N:
        answer += p
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not (-1 < nx < 29 and -1 < ny < 29):
            continue

        if visited[nx][ny]:
            continue

        visited[nx][ny] = 1
        dfs(nx, ny, cnt + 1, p * percent[i] * 0.01)
        visited[nx][ny] = 0


N, *percent = map(int, input().split())

visited = [[0] * 29 for _ in range(29)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
answer = 0

visited[14][14] = 1
dfs(14, 14, 0, 1)

print(answer)
