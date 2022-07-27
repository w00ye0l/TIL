t = int(input())

for i in range(1, t + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    max_ = arr[-1]
    earn = 0

    for j in range(n - 2, -1, -1):
        if arr[j] >= max_:
            max_ = arr[j]
        else:
            earn += max_ - arr[j]

    print(f'#{i} {earn}')
