N = int(input())

dp = [0, 3]

for i in range(2, N + 1):
    dp.append(dp[i - 1] + i * (i + 1) * 3 // 2)
        
print(dp[N])