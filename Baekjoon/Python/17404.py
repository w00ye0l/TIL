MAX = 1000 * 1000 + 1

n = int(input())

cost = []
dp = [[0 for _ in range(3)] for _ in range(n)]
answer = MAX

for _ in range(n):
    cost.append(list(map(int, input().split())))

for k in range(3):
    for i in range(n):
        if i == 0:
            dp[i] = [MAX, MAX, MAX]
            dp[i][k] = cost[0][k]
        else:
            dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + cost[i][0]
            dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + cost[i][1]
            dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + cost[i][2]

    for i in range(3):
        if i == k:
            continue
        answer = min(answer, dp[n - 1][i])

print(answer)
