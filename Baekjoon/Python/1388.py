n, m = map(int, input().split())
stack_ = []


def dfs():
    (y, x) = stack_.pop()
    visited[y][x] = 1

    if flo[y][x] == '-':
        ny = y
        nx = x + 1

    elif flo[y][x] == '|':
        ny = y + 1
        nx = x

    if ny < n and nx < m:
        if flo[ny][nx] == flo[y][x]:
            if visited[ny][nx] == 0:
                stack_.append((ny, nx))
                dfs()

    return 1


flo = []
for _ in range(n):
    flo.append(list(input()))

visited = [[0] * m for _ in range(n)]

sum_ = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == 0:
            stack_.append((i, j))
            sum_ += dfs()

print(sum_)
