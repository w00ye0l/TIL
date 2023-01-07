n = int(input())

arr = list(map(int, input().split()))
reverse_arr = arr[::-1]

dp = [[1 for _ in range(n)] for _ in range(2)]

for i in range(n):
    for j in range(i, -1, -1):
        if arr[i] > arr[j]:
            dp[0][i] = max(dp[0][i], dp[0][j] + 1)

        if reverse_arr[i] > reverse_arr[j]:
            dp[1][i] = max(dp[1][i], dp[1][j] + 1)

dp[1] = dp[1][::-1]

result = 0
for i in range(n):
    if result < dp[0][i] + dp[1][i] - 1:
        result = dp[0][i] + dp[1][i] - 1

print(result)
