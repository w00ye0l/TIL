dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(i, j):
    stack_ = []
    stack_.append((i, j))
    arr[i][j] = 2

    while stack_:
        x, y = stack_.pop()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if not (-1 < nx < m and -1 < ny < n):
                continue

            if arr[nx][ny]:
                continue

            if arr[nx][ny] == 0:
                arr[nx][ny] = 2
                stack_.append((nx, ny))


m, n = map(int, input().split())

arr = []

for _ in range(m):
    arr.append(list(map(int, input())))

for i in range(n):
    if arr[0][i] == 0:
        bfs(0, i)

if arr[m - 1].count(2):
    print("YES")
else:
    print("NO")
