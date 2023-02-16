import sys

sys.setrecursionlimit(10**9)

f, s, g, u, d = map(int, input().split())

dp = [f + 1 for _ in range(f + 1)]
cur = s
dp[cur] = 0


def move(x):
    if x + u <= f:
        if dp[x + u] > dp[x] + 1:
            dp[x + u] = dp[x] + 1
            move(x + u)

    if x - d > 0:
        if dp[x - d] > dp[x] + 1:
            dp[x - d] = dp[x] + 1
            move(x - d)


move(cur)

if dp[g] == f + 1:
    print("use the stairs")
else:
    print(dp[g])
