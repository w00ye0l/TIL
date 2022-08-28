dy = [0, 1]
dx = [1, 0]


def dfs():
    stack = []
    stack.append((0, 0))

    while stack:
        (y, x) = stack.pop()
        visited[y][x] = 1

        for i in range(2):
            ny = y + (dy[i] * board[y][x])
            nx = x + (dx[i] * board[y][x])

            if ny < n and nx < n:
                if not visited[ny][nx]:
                    stack.append((ny, nx))

    return


n = int(input())

board = []
visited = [[0] * n for _ in range(n)]
for _ in range(n):
    board.append(list(map(int, input().split())))

dfs()

if visited[n - 1][n - 1]:
    print("HaruHaru")
else:
    print("Hing")
