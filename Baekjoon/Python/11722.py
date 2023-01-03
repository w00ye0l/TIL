n = int(input())

arr = list(map(int, input().split()))
dp = [1] * n

for i in range(n):
    for j in reversed(range(0, i)):
        if arr[i] < arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
