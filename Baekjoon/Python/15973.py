x1s, y1s, x1e, y1e = map(int, input().split())
x2s, y2s, x2e, y2e = map(int, input().split())

if x1s > x2s:
    x1s, x2s = x2s, x1s
    x1e, x2e = x2e, x1e

if x1e < x2s:
    xx = 0
elif x1e == x2s:
    xx = 1
else:
    xx = 2

if y1s > y2s:
    y1s, y2s = y2s, y1s
    y1e, y2e = y2e, y1e

if y1e < y2s:
    yy = 0
elif y1e == y2s:
    yy = 1
else:
    yy = 2

if xx == 2 and yy == 2:
    print("FACE")
elif (xx == 1 and yy == 2) or (xx == 2 and yy == 1):
    print("LINE")
elif xx == 1 and yy == 1:
    print("POINT")
else:
    print("NULL")
