n = int(input())

num = list(map(int, input().split()))

if n == 1:
    num.sort()

    print(sum(num[:5]))
else:
    num[0] = min(num[0], num[5])
    num[1] = min(num[1], num[4])
    num[2] = min(num[2], num[3])

    min_num = num[:3]
    min_num.sort()

    three = sum(min_num[:3])
    two = sum(min_num[:2])
    one = min_num[0]

    top = 4 * three + 4 * (n - 2) * two + (n - 2) ** 2 * one
    side = 4 * (n - 1) * two + 4 * (n - 1) * (n - 2) * one

    print(top + side)
