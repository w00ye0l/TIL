n, m = map(int, input().split())

lecture = list(map(int, input().split()))
num = [i for i in range(n - 1)]


start, end = max(lecture), sum(lecture)

while start <= end:
    mid = (start + end) // 2

    sum_, cnt = 0, 0

    for i in range(n):
        if sum_ + lecture[i] > mid:
            sum_ = 0
            cnt += 1

        sum_ += lecture[i]

    if sum_ != 0:
        cnt += 1

    if cnt > m:
        start = mid + 1
    else:
        end = mid - 1

print(start)
