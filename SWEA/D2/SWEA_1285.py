t = int(input())

for tt in range(1, t + 1):
    n = int(input())

    stone = list(map(int, input().split()))
    gap = []

    for i in range(n):
        gap.append(abs(0 - stone[i]))

    min_ = min(gap)
    cnt = gap.count(min_)

    print(f'#{tt} {min_} {cnt}')
