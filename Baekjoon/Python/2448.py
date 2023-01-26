n = int(input())

arr = [[" "] * 2 * n for _ in range(n)]


def star(x, y, n):
    if n == 3:
        arr[x][y], arr[x + 1][y - 1], arr[x + 1][y + 1] = "*", "*", "*"
        arr[x + 2][y - 2 : y + 3] = ["*"] * 5

    else:
        star(x, y, n // 2)
        star(x + n // 2, y - n // 2, n // 2)
        star(x + n // 2, y + n // 2, n // 2)


star(0, n - 1, n)

for i in range(n):
    print("".join(arr[i]))
