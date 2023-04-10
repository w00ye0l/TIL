def ccw(a, b, c):
    temp = (a[0] * b[1]) + (b[0] * c[1]) + (c[0] * a[1])
    temp -= (a[0] * c[1]) + (b[0] * a[1]) + (c[0] * b[1])

    if temp > 0:
        return 1
    elif temp < 0:
        return -1
    else:
        return 0


x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
a, b, c, d = (x1, y1), (x2, y2), (x3, y3), (x4, y4)

result1 = ccw(a, b, c) * ccw(a, b, d)
result2 = ccw(c, d, a) * ccw(c, d, b)

if (result1 < 0) and (result2 < 0):
    print(1)
else:
    print(0)
