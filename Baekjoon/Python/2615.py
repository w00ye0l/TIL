def game():
    for i in range(19):
        for j in range(19):
            if board[i][j]:
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    cnt = 1

                    while 0 <= ni < 19 and 0 <= nj < 19 and board[ni][nj] == board[i][j]:
                        cnt += 1

                        if cnt == 5:
                            if 0 <= ni + di[k] < 19 and 0 <= nj + dj[k] < 19:
                                if board[ni + di[k]][nj + dj[k]] == board[ni][nj]:
                                    break

                            if 0 <= i - di[k] < 19 and 0 <= j - dj[k] < 19:
                                if board[i - di[k]][j - dj[k]] == board[i][j]:
                                    break
                            return board[i][j], i+1, j+1

                        ni += di[k]
                        nj += dj[k]

    return 0, -1, -1


di = [1, 1, 0, -1]
dj = [0, 1, 1, 1]

board = [list(map(int, input().split())) for _ in range(19)]

winner, x, y = game()
if not winner:
    print(winner)
else:
    print(winner)
    print(x, y)
