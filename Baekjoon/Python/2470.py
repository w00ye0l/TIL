import math

n = int(input())

liq = list(map(int, input().split()))

liq.sort()

start = 0
end = n - 1
min_ = math.inf
result = [liq[start], liq[end]]

while start < end:
    if min_ > abs(liq[start] + liq[end]):
        min_ = abs(liq[start] + liq[end])
        result[0] = liq[start]
        result[1] = liq[end]

        if liq[start] + liq[end] == 0:
            break

    if liq[start] + liq[end] <= 0:
        start += 1
    else:
        end -= 1

print(*result)
