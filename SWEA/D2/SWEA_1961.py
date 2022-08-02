t = int(input())

for i in range(1, t + 1):
    n = int(input())
    d = []

    for j in range(n):
        d.append(list(map(int, input().split())))

    print(f'#{i}')

    for a in range(n):
        for b in range(n):
            print(f'{d[n-b-1][a]}', end='')
        print(end=' ')
        for b in range(n):
            print(f'{d[n-a-1][n-b-1]}', end='')
        print(end=' ')
        for b in range(n):
            print(f'{d[b][n-a-1]}', end='')
        print()
