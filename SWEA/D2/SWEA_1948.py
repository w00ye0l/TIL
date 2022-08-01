cal = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

t = int(input())

for i in range(1, t + 1):
    m1, d1, m2, d2 = map(int, input().split())
    sum_days = 0

    if m1 == m2:
        sum_days = d2 - d1 + 1
    else:
        j = 1
        sum_days += cal[m1] - d1

        while m1 + j != m2:
            sum_days += cal[m1 + j]
            j += 1
        sum_days += d2 + 1

    print(f'#{i} {sum_days}')
