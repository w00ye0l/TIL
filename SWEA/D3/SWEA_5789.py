for t in range(1, int(input()) + 1):
    n, q = map(int, input().split())

    box = [0 for _ in range(n)]

    change = []
    for _ in range(q):
        l, r = map(int, input().split())
        change.append((l, r))

    for i in range(1, q + 1):
        for j in range(change[i - 1][0] - 1, change[i - 1][1]):
            box[j] = i

    print(f'#{t} {" ".join(map(str, box))}')
