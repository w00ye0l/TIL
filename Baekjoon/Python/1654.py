ans = 0


def b_s(arr, target, start, end):
    global ans

    if start > end:
        return ans

    mid = (start + end) // 2

    cnt = 0
    for a in arr:
        cnt += a // mid

    if cnt < target:
        return b_s(arr, target, start, mid - 1)
    else:
        ans = mid
        return b_s(arr, target, mid + 1, end)


k, n = map(int, input().split())

line = []
for _ in range(k):
    line.append(int(input()))

line.sort(reverse=True)

print(b_s(line, n, 1, line[0]))
