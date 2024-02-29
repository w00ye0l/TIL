for _ in range(int(input())):
    x, y = map(int, input().split())

    dis = y - x
    d = int(dis ** (1 / 2))

    if dis == d**2:
        answer = 2 * d - 1
    elif dis > d**2 + d:
        answer = 2 * d + 1
    else:
        answer = 2 * d

    print(answer)
