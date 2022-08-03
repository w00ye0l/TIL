t = int(input())

for i in range(1, t + 1):
    n, m = map(int, input().split())

    num = [list(map(int, input().split())) for _ in range(n)]
    fly = []

    for j in range(n-m+1):
        for k in range(n-m+1):
            fly.append(num[j][k] + num[j][k + 1] +
                       num[j + 1][k] + num[j + 1][k + 1])

    print(f'# {i} {max(fly)}')
