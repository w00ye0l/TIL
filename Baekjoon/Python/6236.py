import sys

input = sys.stdin.readline


def check(mid):
    temp = 0
    cnt = 0

    for i in range(n):
        if temp < money[i]:
            cnt += 1
            temp = mid

        temp -= money[i]

    if cnt <= m:
        return True
    else:
        return False


n, m = map(int, input().split())

money = [int(input()) for _ in range(n)]

start, end = max(money), sum(money)
result = 0

while start <= end:
    mid = (start + end) // 2

    if check(mid):
        result = mid
        end = mid - 1
    else:
        start = mid + 1

print(result)
