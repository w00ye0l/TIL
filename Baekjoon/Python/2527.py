for _ in range(4):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())

    xy = [[x1, x2, x3, x4], [y1, y2, y3, y4]]

    check = ['', '']
    for i in range(2):
        c = [0] * 50002

        for j in range(xy[i][0], xy[i][1] + 1):
            c[j] += 1

        for j in range(xy[i][2], xy[i][3] + 1):
            c[j] += 1

        if c.count(2) == 1:
            check[i] = 'd'
        elif c.count(2) > 1:
            check[i] = 'l'
        else:
            check[i] = 'none'

    if check[0] == 'd' and check[1] == 'd':
        print('c')
    elif check[0] == 'l' and check[1] == 'l':
        print('a')
    elif check[0] == 'none' or check[1] == 'none':
        print('d')
    else:
        print('b')
