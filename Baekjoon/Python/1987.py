r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
answer = 1


def bfs(x, y):
    global answer

    q = set([(x, y, board[x][y])])

    while q:
        x, y, ans = q.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (-1 < nx < r and -1 < ny < c):
                continue

            # in 문법이 set이 deque보다 탐색 속도가 빠름
            # set : O(1), deque : O(n)
            if board[nx][ny] in ans:
                continue

            q.add((nx, ny, ans + board[nx][ny]))
            answer = max(answer, len(ans) + 1)


bfs(0, 0)

print(answer)
