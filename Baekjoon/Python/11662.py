def dist(t):
    sx = ax * t + bx * (1 - t)
    sy = ay * t + by * (1 - t)
    ex = cx * t + dx * (1 - t)
    ey = cy * t + dy * (1 - t)

    return ((sx - ex) ** 2 + (sy - ey) ** 2) ** 0.5


def threeSearch(left, right):
    while abs(right - left) > 1e-9:
        left3 = (2 * left + right) / 3
        right3 = (left + 2 * right) / 3

        if dist(left3) > dist(right3):
            left = left3
        else:
            right = right3

    return dist(left)


ax, ay, bx, by, cx, cy, dx, dy = map(int, input().split())
print(f"{threeSearch(0, 1):.10f}")
