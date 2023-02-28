import sys

MIN = sys.maxsize

n = int(input())

liq = list(map(int, input().split()))
liq.sort()

for first in range(n - 2):
    second = first + 1
    third = n - 1

    while second < third:
        sum_ = liq[first] + liq[second] + liq[third]

        if MIN > abs(sum_):
            MIN = abs(sum_)
            result = [liq[first], liq[second], liq[third]]

        if sum_ == 0:
            break

        if sum_ <= 0:
            second += 1
        else:
            third -= 1

    if sum_ == 0:
        break

print(*result)
