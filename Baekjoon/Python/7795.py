t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    result = 0

    for i in b:
        start, end = 0, n - 1
        idx = n

        while start <= end:
            mid = (start + end) // 2

            if i < a[mid]:
                idx = min(idx, mid)
                end = mid - 1
            else:
                start = mid + 1

        result += n - idx

    print(result)
