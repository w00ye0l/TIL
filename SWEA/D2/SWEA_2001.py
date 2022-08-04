t = int(input())

for i in range(1, t + 1):
    n, m = map(int, input().split())

    num = [list(map(int, input().split())) for _ in range(n)]
    fly = [[0] * (n - 1) for _ in range(n - m + 1)]

    for j in range(n - m + 1):
        for k in range(n - m + 1):
            for a in range(m):
                for b in range(m):
                    fly[j][k] += num[j + a][k + b]

    print(f'#{i} {max(map(max, fly))}')
