W, H, N = map(int, input().split())

if N % 2 == 0:
    print(2 * H * ((N - 2) / 4))
else:
    print(2 * H * (N - 1) ** 2 / (4 * N))
