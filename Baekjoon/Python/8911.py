import sys

input = sys.stdin.readline

for _ in range(int(input())):
    move = input().rstrip()

    x, y = 0, 0
    xlist, ylist = [0], [0]
    d = 0

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    for m in move:
        if m == "F":
            x += dx[d]
            y += dy[d]

            xlist.append(x)
            ylist.append(y)

        elif m == "B":
            x -= dx[d]
            y -= dy[d]

            xlist.append(x)
            ylist.append(y)

        elif m == "L":
            d = (d + 1) % 4

        elif m == "R":
            d = (d - 1) % 4

    r1, r2 = min(xlist), max(xlist)
    c1, c2 = min(ylist), max(ylist)

    print((r2 - r1) * (c2 - c1))
