D, K = map(int, input().split())

dp = [(1, 0), (0, 1)]

for i in range(2, D):
    dp.append(tuple(x + y for x, y in zip(dp[i - 1], dp[i - 2])))

ac, bc = dp[-1]
A = 1

while True:
    if (K - A * ac) % bc == 0:
        B = (K - A * ac) // bc
        break

    A += 1

print(A, B, sep="\n")
