t = int(input())

for tt in range(1, t + 1):
    n = int(input())

    s = ""
    len_ = 0
    for i in range(n):
        ci, ki = input().split()
        r_ki = int(ki)
        len_ += r_ki
        s += ci * r_ki

    print(f'#{tt}')
    for i in range(len_):
        if i % 10 == 9:
            print(s[i])
        else:
            print(s[i], end='')
    print()
