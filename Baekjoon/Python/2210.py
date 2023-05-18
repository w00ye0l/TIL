def dfs(x, y, result):
    if len(result) == 6:
        answer.add(result)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not (-1 < nx < 5 and -1 < ny < 5):
            continue

        dfs(nx, ny, result + str(nums[nx][ny]))


nums = [list(map(int, input().split())) for _ in range(5)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = set()

for i in range(5):
    for j in range(5):
        dfs(i, j, str(nums[i][j]))

print(len(answer))
