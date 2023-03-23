n = int(input())

arr = list(map(int, input().split()))

dp = [1 for _ in range(n)]

for i in range(1, n):
    for j in range(i - 1, -1, -1):
        if arr[i] < arr[j]:
            dp[i] = max(dp[j] + 1, dp[i])

print(n - max(dp))
