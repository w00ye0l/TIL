n = int(input())

child = [int(input()) for _ in range(n)]

dp = [1] * n

for i in range(n):
    for j in range(i - 1, -1, -1):
        if child[i] > child[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))
