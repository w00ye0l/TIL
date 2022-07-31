k = int(input())

for i in range(1, k + 1):
    score = list(map(int, input().split()))
    n = score[0]
    score = score[1:]
    gap = []

    score.sort(reverse=True)

    for j in range(1, n):
        gap.append(score[j - 1] - score[j])

    gap.sort(reverse=True)

    print(f'Class {i}')
    print(f'Max {score[0]}, Min {score[-1]}, Largest gap {gap[0]}')
