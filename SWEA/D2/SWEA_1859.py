t = int(input())

for i in range(1, t + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    earn = 0
    l = len(arr)

    while l:
        idx = 0
        max = 0
        cost = 0

        for j in range(l):
            if arr[j] > max:
                max = arr[j]
                idx = j

        for k in range(idx):
            cost += arr[k]

        earn += max * idx - cost
        arr = arr[idx + 1:]
        l -= idx + 1

    print(f'#{i} {earn}')
