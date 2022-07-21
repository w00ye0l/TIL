t = int(input())

for i in range(1, t+1):
    n = input()
    yy = int(n[:4])
    mm = int(n[4:6])
    dd = int(n[6:])

    if yy <= 0 or mm <= 0 or dd <= 0:
        print(f'#{i} -1')
        continue
    elif mm < 8:
        if mm == 2 and dd > 28:
            print(f'#{i} -1')
            continue
        elif mm % 2 == 0 and dd > 30:
            print(f'#{i} -1')
            continue
        elif mm % 2 == 1 and dd > 31:
            print(f'#{i} -1')
            continue
    else:
        if mm % 2 == 0 and dd > 31:
            print(f'#{i} -1')
            continue
        elif mm % 2 == 1 and dd > 30:
            print(f'#{i} -1')
            continue

    print(f'#{i} {yy:04d}/{mm:02d}/{dd:02d}')
