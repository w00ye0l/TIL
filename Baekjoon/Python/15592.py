coor = []

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())


if y2 < y4 and y3 < y1:
    if x3 < x2 < x4:
        x2 = x3

    elif x3 < x1 < x4:
        x1 = x4

elif x3 < x1 and x2 < x4:
    if y3 < y2 < y4:
        y2 = y3

    elif y3 < y1 < y4:
        y1 = y4

print((x2 - x1) * (y2 - y1))
