import math

x, y, c = map(float, input().split())

left, right = 0, min(x, y)

while right - left >= 0.001:
    temp = (left + right) / 2
    h1 = math.sqrt(pow(x, 2) - pow(temp, 2))
    h2 = math.sqrt(pow(y, 2) - pow(temp, 2))

    ans = (h1 * h2) / (h1 + h2)

    if ans >= c:
        left = temp
    else:
        right = temp

print(f"{right:.3f}")
