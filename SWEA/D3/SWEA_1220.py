for t in range(1, 11):
    table = []

    for _ in range(int(input())):
        table.append(list(map(int, input().split())))

    cnt = 0
    for j in range(100):
        flag = False
        for i in range(100):
            if table[i][j] == 1:
                flag = True

            if table[i][j] == 2 and flag == True:
                cnt += 1
                flag = False

    print(f"#{t} {cnt}")
