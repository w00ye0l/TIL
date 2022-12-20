def nqueen(idx):
    global cnt

    if idx == n:
        cnt += 1
        return

    for i in range(n):
        board[idx] = i

        if check(idx):
            nqueen(idx + 1)


def check(idx):
    for i in range(idx):
        if board[idx] == board[i] or idx - i == abs(board[idx] - board[i]):
            return 0

    return 1


n = int(input())
board = [0] * n
cnt = 0

nqueen(0)

print(cnt)
