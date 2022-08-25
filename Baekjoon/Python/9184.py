import sys
input = sys.stdin.readline


def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    if arr[a][b][c]:
        return arr[a][b][c]

    if a < b < c:
        arr[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        return arr[a][b][c]

    arr[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + \
        w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
    return arr[a][b][c]


arr = [[[0] * 21 for _ in range(21)] for _ in range(21)]

while True:
    a, b, c = map(int, input().split())

    end = (-1, -1, -1)
    if (a, b, c) == end:
        break

    print(f'w({a}, {b}, {c}) = {w(a, b, c)}')
