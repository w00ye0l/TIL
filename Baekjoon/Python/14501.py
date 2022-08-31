n = int(input())

dp = [0] * (n + 1)

consult = []
for _ in range(n):
    consult.append(list(map(int, input().split())))

for i in range(n - 1, -1, -1):
    if i + consult[i][0] > n:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], consult[i][1] + dp[i + consult[i][0]])

print(dp[0])
