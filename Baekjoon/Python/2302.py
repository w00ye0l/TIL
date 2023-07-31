N = int(input())
M = int(input())

dp = [1, 1, 2, 3]

for i in range(4, N + 1):
    dp.append(dp[i - 1] + dp[i - 2])

idx = 0
answer = 1

for _ in range(M):
    fix = int(input())

    answer *= dp[fix - idx - 1]
    idx = fix

answer *= dp[N - idx]

print(answer)
