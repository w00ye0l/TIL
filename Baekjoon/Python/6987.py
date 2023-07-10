from itertools import combinations


def bt(cnt):
    global ans

    if cnt == 15:
        if sum(map(sum, result)) == 0:
            ans = 1
            return
        return

    i, j = game[cnt]
    for x, y in ((0, 2), (1, 1), (2, 0)):
        if result[i][x] > 0 and result[j][y] > 0:
            result[i][x] -= 1
            result[j][y] -= 1

            bt(cnt + 1)

            result[i][x] += 1
            result[j][y] += 1


answer = []

for _ in range(4):
    arr = list(map(int, input().split()))

    result = [[0] * 3 for _ in range(6)]

    for i in range(18):
        result[i // 3][i % 3] = arr[i]

    game = tuple(combinations(range(6), 2))

    ans = 0
    bt(0)

    answer.append(ans)

print(*answer)
