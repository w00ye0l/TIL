import sys

input = sys.stdin.readline

while True:
    n, m = map(float, input().split())

    n = int(n)
    m = int(m * 100 + 0.5)

    if n == 0 and m == 0:
        break

    dp = [0 for _ in range(m + 1)]

    for _ in range(n):
        c, p = map(float, input().split())

        c = int(c)
        p = int(p * 100 + 0.5)

        if p > m:
            continue

        for t in range(p, m + 1):
            dp[t] = max(dp[t], dp[t - p] + c)

    print(dp[m])
