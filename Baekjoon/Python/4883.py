import sys

input = sys.stdin.readline

t = 0
while True:
    t += 1
    N = int(input())

    if N == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0] * 3 for _ in range(N)]

    dp[0][0], dp[0][1], dp[0][2] = float("inf"), graph[0][1], graph[0][1] + graph[0][2]

    for i in range(1, N):
        dp[i][0] = graph[i][0] + min(dp[i - 1][:2])
        dp[i][1] = graph[i][1] + min(*dp[i - 1], dp[i][0])
        dp[i][2] = graph[i][2] + min(*dp[i - 1][1:], dp[i][1])

    print(f"{t}. {dp[-1][1]}")
