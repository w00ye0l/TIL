import sys

input = sys.stdin.readline


def round_num(n):
    if n - int(n) >= 0.5:
        return int(n) + 1
    else:
        return int(n)


n = int(input())

if n == 0:
    print(0)
else:
    score = []
    for _ in range(n):
        score.append(int(input()))

    score.sort()

    cut = round_num(n * 0.15)
    if cut != 0:
        score = score[cut:-cut]

    print(round_num(sum(score) / (n - 2 * cut)))


# import sys
# import decimal

# input = sys.stdin.readline

# context = decimal.getcontext()

# context.rounding = decimal.ROUND_HALF_UP

# n = int(input())

# if n == 0:
#     print(0)
# else:
#     score = []
#     for _ in range(n):
#         score.append(int(input()))

#     score.sort()

#     cut = int(round(decimal.Decimal(str(n * 0.15)), 0))
#     if cut != 0:
#         score = score[cut:-cut]

#     print(round(decimal.Decimal(sum(score) / (n - 2 * cut)), 0))
