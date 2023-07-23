import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())

route = [[] for _ in range(N + 1)]

for _ in range(K):
    a, b, c = map(int, input().split())

    if a < b:
        route[a].append((b, c))

dp = [[0] * (N + 1) for _ in range(N + 1)]

for n, w in route[1]:
    dp[n][2] = max(dp[n][2], w)

for i in range(2, M + 1):
    for j in range(1, N + 1):
        if dp[j][i] != 0:
            for n, w in route[j]:
                dp[n][i + 1] = max(dp[n][i + 1], dp[j][i] + w)

print(max(dp[N][: M + 1]))
