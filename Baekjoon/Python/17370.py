import sys

sys.setrecursionlimit(10**9)


def dfs(x, y, cnt, d):
    global answer

    if board[x][y]:
        if cnt == N:
            answer += 1
            return

    if board[x][y]:
        return

    if cnt > N:
        return

    board[x][y] = 1

    for i in range(2):
        nx = x + dx[directions[d][i]]
        ny = y + dy[directions[d][i]]

        if not (-1 < nx < 100 and -1 < ny < 100):
            continue

        dfs(nx, ny, cnt + 1, directions[d][i])

    board[x][y] = 0


N = int(input())

dx = [-1, -1, 1, 1, 1, -1]
dy = [0, 1, 1, 0, -1, -1]
directions = [(1, 5), (0, 2), (1, 3), (2, 4), (3, 5), (0, 4)]
board = [[0 for _ in range(100)] for _ in range(100)]
answer = 0

board[51][50] = 1
dfs(50, 50, 0, 0)

print(answer)
