n, new_point, p = map(int, input().split())

if n > 0:
    score = list(map(int, input().split()))

    rank = 1
    for i in range(n):
        if new_point < score[i]:
            rank += 1
        elif new_point > score[i]:
            break

        if i == p - 1:
            rank = -1

    print(rank)
else:
    print(1)
