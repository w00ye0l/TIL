import copy


def top(x, y):
    cnt = 0

    for i in range(x - 1, -1, -1):
        if office[i][y] == 0:
            cnt += 1
            office[i][y] = -1
        elif office[i][y] == 6:
            break

    return cnt


def right(x, y):
    cnt = 0

    for i in range(y + 1, m):
        if office[x][i] == 0:
            cnt += 1
            office[x][i] = -1
        elif office[x][i] == 6:
            break

    return cnt


def bottom(x, y):
    cnt = 0

    for i in range(x + 1, n):
        if office[i][y] == 0:
            cnt += 1
            office[i][y] = -1
        elif office[i][y] == 6:
            break

    return cnt


def left(x, y):
    cnt = 0

    for i in range(y - 1, -1, -1):
        if office[x][i] == 0:
            cnt += 1
            office[x][i] = -1
        elif office[x][i] == 6:
            break

    return cnt


def check(idx):
    global office, min_

    if idx == cctvCnt:
        result = 0

        for i in range(n):
            for j in range(m):
                if office[i][j] == 0:
                    result += 1

        min_ = min(min_, result)

        return min_

    r, c = cctv[idx][0], cctv[idx][1]
    temp = copy.deepcopy(office)

    if office[r][c] == 1:
        for i in range(4):
            if i == 0:
                top(r, c)
            elif i == 1:
                right(r, c)
            elif i == 2:
                bottom(r, c)
            elif i == 3:
                left(r, c)

            check(idx + 1)

            office = copy.deepcopy(temp)

    elif office[r][c] == 2:
        for i in range(2):
            if i == 0:
                top(r, c), bottom(r, c)
            elif i == 1:
                left(r, c), right(r, c)

            check(idx + 1)

            office = copy.deepcopy(temp)

    elif office[r][c] == 3:
        for i in range(4):
            if i == 0:
                top(r, c), right(r, c)
            elif i == 1:
                right(r, c), bottom(r, c)
            elif i == 2:
                bottom(r, c), left(r, c)
            elif i == 3:
                left(r, c), top(r, c)

            check(idx + 1)

            office = copy.deepcopy(temp)

    elif office[r][c] == 4:
        for i in range(4):
            if i == 0:
                top(r, c), right(r, c), left(r, c)
            elif i == 1:
                top(r, c), right(r, c), bottom(r, c)
            elif i == 2:
                right(r, c), bottom(r, c), left(r, c)
            elif i == 3:
                top(r, c), bottom(r, c), left(r, c)

            check(idx + 1)

            office = copy.deepcopy(temp)

    elif office[r][c] == 5:
        top(r, c), right(r, c), bottom(r, c), left(r, c)

        check(idx + 1)

        office = copy.deepcopy(temp)


n, m = map(int, input().split())
min_ = 100
office = []
cctv = []
cctvCnt = 0

for _ in range(n):
    office.append(list(map(int, input().split())))


for i in range(n):
    for j in range(m):
        if office[i][j] != 0 and office[i][j] != 6:
            cctv.append((i, j))
            cctvCnt += 1

if cctvCnt > 0:
    check(0)
else:
    result = 0
    for i in range(n):
        for j in range(m):
            if office[i][j] == 0:
                result += 1

    min_ = min(min_, result)

print(min_)
