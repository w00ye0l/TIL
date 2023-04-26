n = int(input())

child = list(map(int, input().split()))
dp = [0] * (n + 1)
max_ = 0

for i in range(n):
    cur = child[i]
    dp[cur] = dp[cur - 1] + 1
    max_ = max(max_, dp[cur])

print(n - max_)
