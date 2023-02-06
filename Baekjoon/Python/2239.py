def bt(cnt):
    if len(zeroList) == cnt:
        for i in range(9):
            print(*sudoku[i], sep="")
        return True

    (x, y) = zeroList[cnt]

    check = [False for _ in range(10)]

    for i in range(9):
        if sudoku[x][i] != 0:
            check[sudoku[x][i]] = True

        if sudoku[i][y] != 0:
            check[sudoku[i][y]] = True

    nx = (x // 3) * 3
    ny = (y // 3) * 3

    for i in range(nx, nx + 3):
        for j in range(ny, ny + 3):
            if sudoku[i][j] != 0:
                check[sudoku[i][j]] = True

    for i in range(1, 10):
        if check[i] == False:
            sudoku[x][y] = i

            if bt(cnt + 1):
                return True

            sudoku[x][y] = 0

    return False


sudoku = []
zeroList = []

for _ in range(9):
    sudoku.append(list(map(int, input())))

for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            zeroList.append((i, j))

bt(0)
