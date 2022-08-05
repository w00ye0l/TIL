for t in range(1, int(input()) + 1):
    n = int(input())

    result = [[0] * n for _ in range(n)]

    x, y = 0, 0
    dir = 0
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    cnt = 1

    for _ in range(n ** 2):
        result[y][x] = cnt
        x += dx[dir]
        y += dy[dir]

        if x < 0 or x >= n or y < 0 or y >= n or result[y][x] != 0:
            x -= dx[dir]
            y -= dy[dir]

            dir = (dir + 1) % 4
            x += dx[dir]
            y += dy[dir]
        cnt += 1

    print(f'#{t}')
    for i in result:
        print(*i)
