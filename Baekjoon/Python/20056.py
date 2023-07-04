def sum_fireball(i, j):
    tm, ts, td, cnt = 0, 0, 0, len(grid[i][j])
    while grid[i][j]:
        m, s, d = grid[i][j].pop(0)
        tm += m
        ts += s
        td += d % 2

    tm //= 5
    ts //= cnt
    if tm:
        if td == 0 or td == cnt:
            for nd in [0, 2, 4, 6]:
                fireball.append([i, j, tm, ts, nd])
        else:
            for nd in [1, 3, 5, 7]:
                fireball.append([i, j, tm, ts, nd])


N, M, K = map(int, input().split())

grid = [[[] for _ in range(N)] for _ in range(N)]
fireball = []
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(M):
    r, c, m, s, d = map(int, input().split())

    fireball.append([r - 1, c - 1, m, s, d])

for _ in range(K):
    while fireball:
        r, c, m, s, d = fireball.pop(0)
        nr = (r + s * dx[d]) % N
        nc = (c + s * dy[d]) % N

        grid[nr][nc].append([m, s, d])

    for i in range(N):
        for j in range(N):
            if len(grid[i][j]) >= 2:
                sum_fireball(i, j)
            elif len(grid[i][j]) == 1:
                fireball.append([i, j] + grid[i][j].pop())

print(sum([f[2] for f in fireball]))
