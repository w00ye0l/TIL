import copy

n = int(input())
k = int(input())

board = []

for _ in range(n):
    board.append(list(map(int, input().split())))

power = list(map(int, input().split()))

result = 0
visited = [-1 for _ in range(k)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def shot():
    score = 0
    temp = copy.deepcopy(board)
    bomb = {}

    for i in range(k):
        for j in range(n):
            if temp[visited[i]][j] >= 10:
                score += temp[visited[i]][j]
                temp[visited[i]][j] = 0

                break

            elif temp[visited[i]][j] > power[i]:
                if not (visited[i], j) in bomb:
                    bomb[(visited[i], j)] = temp[visited[i]][j]

                temp[visited[i]][j] -= power[i]

                break

            elif 0 < temp[visited[i]][j] <= power[i]:
                add = (
                    bomb[(visited[i], j)]
                    if (visited[i], j) in bomb
                    else temp[visited[i]][j]
                )
                temp[visited[i]][j] = 0

                for l in range(4):
                    nx = visited[i] + dx[l]
                    ny = j + dy[l]

                    if not (-1 < nx < n and -1 < ny < n):
                        continue

                    if temp[nx][ny] == 0:
                        temp[nx][ny] = int(add / 4)

                score += add

                break

    return score


def bt(cnt):
    global result

    if cnt == k:
        result = max(result, shot())

        return

    for i in range(n):
        visited[cnt] = i
        bt(cnt + 1)


bt(0)

print(result)
