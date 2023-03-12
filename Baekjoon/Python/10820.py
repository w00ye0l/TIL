import sys

while True:
    line = sys.stdin.readline().rstrip("\n")

    if not line:
        break

    l, u, d, s = 0, 0, 0, 0

    for a in line:
        if a.islower():
            l += 1
        elif a.isupper():
            u += 1
        elif a.isdigit():
            d += 1
        elif a.isspace():
            s += 1

    print(l, u, d, s)
