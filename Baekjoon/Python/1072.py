x, y = map(int, input().split())

z = (y * 100) // x

if z >= 99:
    print(-1)
else:
    start, end = 0, 1000000000
    result = 0

    while start <= end:
        mid = (start + end) // 2

        temp = int((y + mid) / (x + mid) * 100)

        if z >= temp:
            start = mid + 1
        else:
            result = mid
            end = mid - 1

    print(result)
