n, m, x, y, k = map(int, input().split())

matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().split())))

orders = list(map(int, input().split()))

dice = [0 for _ in range(6)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for order in orders:
    nx = x + dx[order - 1]
    ny = y + dy[order - 1]

    if not (-1 < nx < n and -1 < ny < m):
        continue

    x, y = nx, ny

    temp = dice[0]
    if order == 1:
        dice[0] = dice[3]
        dice[3] = dice[5]
        dice[5] = dice[2]
        dice[2] = temp
    elif order == 2:
        dice[0] = dice[2]
        dice[2] = dice[5]
        dice[5] = dice[3]
        dice[3] = temp
    elif order == 3:
        dice[0] = dice[4]
        dice[4] = dice[5]
        dice[5] = dice[1]
        dice[1] = temp
    elif order == 4:
        dice[0] = dice[1]
        dice[1] = dice[5]
        dice[5] = dice[4]
        dice[4] = temp

    if matrix[x][y] == 0:
        matrix[x][y] = dice[5]
    else:
        dice[5] = matrix[x][y]
        matrix[x][y] = 0

    print(dice[0])
