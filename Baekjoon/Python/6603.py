import itertools

while True:
    num = list(map(int, input().split()))

    n = num[0]
    num = num[1:]

    if n == 0:
        break

    temp = list(set(itertools.combinations(num, 6)))

    lotto = []
    for t in temp:
        lotto.append(list(t))

    lotto.sort()

    for l in lotto:
        print(*l)
    print()
