def Win(player):
    flag = False

    for i in range(3):
        if board[i][0] == player:
            if board[i][0] == board[i][1] == board[i][2]:
                flag = True
        if board[0][i] == player:
            if board[0][i] == board[1][i] == board[2][i]:
                flag = True

    if board[0][0] == player:
        if board[0][0] == board[1][1] == board[2][2]:
            flag = True

    if board[0][2] == player:
        if board[0][2] == board[1][1] == board[2][0]:
            flag = True

    return flag


while True:
    arr = input()

    if arr == "end":
        break

    board = []
    totalXCnt, totalOCnt = 0, 0
    flag1 = True

    for i in range(0, 7, 3):
        temp = []
        for j in range(3):
            temp.append(arr[i + j])
            if arr[i + j] == "X":
                totalXCnt += 1
            elif arr[i + j] == "O":
                totalOCnt += 1

        board.append(temp)

    xWin = Win("X")
    oWin = Win("O")

    if xWin and not oWin and totalXCnt - totalOCnt == 1:
        print("valid")
    elif not xWin and oWin and totalXCnt == totalOCnt:
        print("valid")
    elif not xWin and not oWin and totalXCnt == 5 and totalOCnt == 4:
        print("valid")
    else:
        print("invalid")
