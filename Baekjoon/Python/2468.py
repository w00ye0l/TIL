import sys
sys.setrecursionlimit(10**6)


def dfs(i, j, k):
    x, y = i, j

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for a in range(4):
        nx = x + dx[a]
        ny = y + dy[a]

        if not (-1 < nx < n and -1 < ny < n):
            continue

        if visited[nx][ny]:
            continue

        if height[nx][ny] > k:
            visited[nx][ny] = 1
            dfs(nx, ny, k)


n = int(input())

height = []
for _ in range(n):
    height.append(list(map(int, input().split())))

answer = 1
for k in range(max(map(max, height))):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(n):
            if height[i][j] > k and not visited[i][j]:
                cnt += 1
                visited[i][j] = 1
                dfs(i, j, k)

    answer = max(answer, cnt)

print(answer)
