H, W, X, Y = map(int, input().split())

B = [list(map(int, input().split())) for _ in range(H + X)]

A = [[0] * W for _ in range(H)]

for i in range(H):
    for j in range(W):
        if i < X or j < Y:
            A[i][j] = B[i][j]
        else:
            A[i][j] = B[i][j] - A[i - X][j - Y]

for i in range(H):
    print(*A[i])
