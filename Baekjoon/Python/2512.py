ans = 0


def b_s(arr, target, start, end):
    global ans

    if start > end:
        return ans

    mid = (start + end) // 2

    sum_ = 0
    for a in arr:
        if a < mid:
            sum_ += a
        else:
            sum_ += mid

    if sum_ <= target:
        ans = mid
        return b_s(arr, target, mid + 1, end)
    else:
        return b_s(arr, target, start, mid - 1)


n = int(input())

req = list(map(int, input().split()))
req.sort(reverse=True)

money = int(input())

print(b_s(req, money, 1, req[0]))
