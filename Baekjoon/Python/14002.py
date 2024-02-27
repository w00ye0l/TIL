N = int(input())
arr = list(map(int, input().split()))

dp = [[[arr[i]], 1] for i in range(N)]
answer = []

for i in range(N):
    for j in range(i):
        if arr[j] < arr[i]:
            if dp[i][1] < dp[j][1] + 1:
                dp[i][1] = dp[j][1] + 1
                dp[i][0] = dp[j][0] + [arr[i]]

for i in range(N):
    if len(answer) < dp[i][1]:
        answer = dp[i][0]

print(len(answer))
print(*answer)
