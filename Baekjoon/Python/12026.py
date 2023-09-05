N = int(input())
arr = list(input())

dp = [float("inf")] * N
dp[0] = 0

for i in range(N):
    now = arr[i]

    for j in range(i + 1, N):
        if now == "B" and arr[j] == "O":
            dp[j] = min(dp[j], (j - i) ** 2 + dp[i])
        elif now == "O" and arr[j] == "J":
            dp[j] = min(dp[j], (j - i) ** 2 + dp[i])
        elif now == "J" and arr[j] == "B":
            dp[j] = min(dp[j], (j - i) ** 2 + dp[i])

if dp[-1] == float("inf"):
    print(-1)
else:
    print(dp[-1])
