ans = 0


def b_s(arr, target, start, end):
    global ans

    if start > end:
        return ans

    mid = (start + end) // 2

    sum_ = 0
    for a in arr:
        if a > mid:
            sum_ += a - mid

    if sum_ < target:
        return b_s(arr, target, start, mid - 1)
    else:
        ans = mid
        return b_s(arr, target, mid + 1, end)


n, m = map(int, input().split())

tree = list(map(int, input().split()))

tree.sort(reverse=True)

print(b_s(tree, m, 1, tree[0]))
