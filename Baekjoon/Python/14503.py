n, m = map(int, input().split())

r, c, d = map(int, input().split())

place = []
for _ in range(n):
    place.append(list(map(int, input().split())))

visited = [[0 for _ in range(m)] for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited[r][c] = 1
cnt = 1

while True:
    wall = 0

    for i in range(4):
        d = (d + 3) % 4
        nr = r + dx[d]
        nc = c + dy[d]

        if place[nr][nc] == 0 and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                r, c = nr, nc
                cnt += 1
                wall = 1
                break

    if wall == 0:
        if place[r - dx[d]][c - dy[d]] == 1:
            print(cnt)
            break
        else:
            r -= dx[d]
            c -= dy[d]
