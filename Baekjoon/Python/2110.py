import sys
input = sys.stdin.readline

ans = 0


def b_s(arr, target, start, end):
    global ans
    pre = arr[0]

    if start > end:
        return ans

    mid = (start + end) // 2

    cnt = 1
    for i in range(1, n):
        if house[i] - pre >= mid:
            cnt += 1
            pre = house[i]

    if cnt >= target:
        ans = max(ans, mid)
        return b_s(arr, target, mid + 1, end)
    else:
        return b_s(arr, target, start, mid - 1)


n, c = map(int, input().split())

house = []
for _ in range(n):
    house.append(int(input()))

house.sort()

print(b_s(house, c, 1, house[-1] - house[0]))
