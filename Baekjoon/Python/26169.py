def bt(x, y, cnt, apple):
    global answer
    if cnt == 3:
        if apple >= 2:
            answer = 1
            return

    for i in range(4):
        flag = False
        nx = x + dx[i]
        ny = y + dy[i]

        if not (-1 < nx < 5 and -1 < ny < 5):
            continue

        if grid[nx][ny] == -1:
            continue

        napple = apple

        if grid[nx][ny] == 1:
            napple = apple + 1
            flag = True
        grid[nx][ny] = -1

        bt(nx, ny, cnt + 1, napple)

        if flag:
            grid[nx][ny] = 1
        else:
            grid[nx][ny] = 0


grid = [list(map(int, input().split())) for _ in range(5)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0

r, c = map(int, input().split())

grid[r][c] = -1

bt(r, c, 0, 0)

print(answer)
