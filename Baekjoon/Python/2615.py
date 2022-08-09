dy = [0, 1, -1, 1]
dx = [1, 0, 1, 1]
N = 19

board = []

for _ in range(N):
    temp_list = list(map(int, input().split()))
    board.append(temp_list)

answer = 0

for y in range(N):
    for x in range(N):
        if board[y][x]:
            for d in range(4):
                stone_count = 1

                ny = y + dy[d]
                nx = x + dx[d]

                while True:
                    if not (-1 < ny < N and -1 < nx < N):
                        break

                    if board[ny][nx] != board[y][x]:
                        break

                    stone_count += 1

                    ny += dy[d]
                    nx += dx[d]

                if stone_count == 5:
                    prev_y = y - dy[d]
                    prev_x = x - dx[d]

                    if not (-1 < prev_y < N and -1 < prev_x < N) or board[y][x] != board[prev_y][prev_x]:
                        print(board[y][x])
                        print(y + 1, x + 1)
                        answer = board[y][x]

if answer == 0:
    print(answer)
