n = int(input())

rgb = []
for _ in range(n):
    rgb.append(list(map(int, input().split())))

dp = [rgb[0]]
for i in range(1, n):
    temp = []
    temp.append(min(dp[i - 1][1], dp[i - 1][2]) + rgb[i][0])
    temp.append(min(dp[i - 1][0], dp[i - 1][2]) + rgb[i][1])
    temp.append(min(dp[i - 1][0], dp[i - 1][1]) + rgb[i][2])

    dp.append(temp)

print(min(dp[-1]))
