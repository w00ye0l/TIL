def matrix_mul(a, b):
    temp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                temp[i][j] += a[i][k] * b[k][j]

            temp[i][j] %= 1000

    return temp


def pow_matrix(arr, n, b):
    result = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        result[i][i] = 1

    while b > 0:
        if b % 2 == 1:
            result = matrix_mul(result, arr)

        b //= 2
        arr = matrix_mul(arr, arr)

    return result


n, b = map(int, input().split())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))


for i in range(n):
    print(*pow_matrix(arr, n, b)[i])
