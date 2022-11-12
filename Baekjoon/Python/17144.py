r, c, t = map(int, input().split())

mise = []

for _ in range(r):
    mise.append(list(map(int, input().split())))

cleaner = []


def spread():
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    temp = [[0 for _ in range(c)] for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if mise[i][j] == -1:
                cleaner.append(i)
            elif mise[i][j] != 0:
                cnt = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if not (-1 < nx < r and -1 < ny < c) or mise[nx][ny] == -1:
                        continue

                    cnt += 1
                    temp[nx][ny] += mise[i][j] // 5

                temp[i][j] -= (mise[i][j] // 5) * cnt

    for i in range(r):
        for j in range(c):
            mise[i][j] += temp[i][j]

    return


def clean(cleaner):
    global r, c
    # 윗부분 회전
    # 왼쪽
    for i in range(cleaner[0] - 1, 0, -1):
        mise[i][0] = mise[i - 1][0]

    # 오른쪽
    for i in range(cleaner[0]):
        mise[i][c - 1] = mise[i + 1][c - 1]

    mise[cleaner[0]][1] = 0

    # 아랫부분 회전
    # 왼쪽
    for i in range(cleaner[1] + 1, r - 1):
        mise[i][0] = mise[i + 1][0]

    # 오른쪽
    for i in range(r - 1, cleaner[1], -1):
        mise[i][c - 1] = mise[i - 1][c - 1]

    mise[cleaner[1]][1] = 0

    # 공통부분
    # 맨위, 맨아래
    for i in range(c - 1):
        mise[0][i] = mise[0][i + 1]
        mise[r - 1][i] = mise[r - 1][i + 1]

    # 공기청정기 라인
    for i in range(c - 1, 0, -1):
        mise[cleaner[0]][i] = mise[cleaner[0]][i - 1]
        mise[cleaner[1]][i] = mise[cleaner[1]][i - 1]


for _ in range(t):
    spread()
    clean(cleaner)

answer = 0
for i in range(r):
    for j in range(c):
        if mise[i][j] > 0:
            answer += mise[i][j]

print(answer)
