t = int(input())

for tt in range(1, t + 1):
    board = []
    for _ in range(9):
        board.append(list(map(int, input().split())))

    result1 = 1
    result2 = 1
    result3 = 1

    for i in range(9):
        chk_l1 = [0] * 10

        for j in range(9):
            chk_l1[board[i][j]] = 1

        if chk_l1.count(1) != 9:
            result1 = 0
            break

    for i in range(9):
        chk_l2 = [0] * 10

        for j in range(9):
            chk_l2[board[j][i]] = 1

        if chk_l2.count(1) != 9:
            result2 = 0
            break

    for i in range(0, 9, 3):
        chk_l3 = [0] * 10

        for j in range(0, 9, 3):
            for a in range(3):
                for b in range(3):
                    chk_l3[board[i+a][j+b]] = 1

            if chk_l3.count(1) != 9:
                result3 = 0
                break

    if result1 * result2 * result3 == 1:
        print(f'#{tt} 1')
    else:
        print(f'#{tt} 0')
