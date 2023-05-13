for _ in range(int(input())):
    N = int(input())
    sum_C, sum_G = 0, 0

    for _ in range(N):
        C, G = input().split()

        sum_C += int(C)
        sum_G += int(C) * float(G)

    print(f"{sum_C} {sum_G / sum_C:.1f}")
