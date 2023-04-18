t = 0

while True:
    t += 1
    flag = False

    o, w = map(int, input().split())

    if o == 0 and w == 0:
        break

    while True:
        order, n = input().split()

        if order == "#" and n == "0":
            if flag:
                print(f"{t} RIP")
            else:
                if o / 2 < w < o * 2:
                    print(f"{t} :-)")
                else:
                    print(f"{t} :-(")

            break

        elif order == "F":
            w += int(n)

        elif order == "E":
            w -= int(n)

            if w <= 0:
                flag = True
