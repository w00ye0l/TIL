t = int(input())

for _ in range(t):
    coor = []
    r_coor = []

    for _ in range(4):
        x, y = map(int, input().split())

        coor.append([x, y])

    coor.sort()

    for i in range(1, 4):
        rx, ry = coor[i][0] - coor[0][0], coor[i][1] - coor[0][1]

        s = rx ** 2 + ry ** 2

        r_coor.append([rx, ry, s])

    if not ((r_coor[0][0] + r_coor[1][0] == r_coor[2][0]) & (r_coor[0][1] + r_coor[1][1] == r_coor[2][1])):
        print(0)
    else:
        if not ((r_coor[0][0] * r_coor[1][0]) + (r_coor[0][1] * r_coor[1][1]) == 0):
            print(0)
        else:
            if not (r_coor[0][2] == r_coor[1][2]):
                print(0)
            else:
                print(1)
