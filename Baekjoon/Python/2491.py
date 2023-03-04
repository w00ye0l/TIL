n = int(input())
arr = list(map(int, input().split()))

big_dp = [1 for _ in range(n)]
small_dp = [1 for _ in range(n)]

for i in range(1, n):
    if arr[i] >= arr[i - 1]:
        big_dp[i] = big_dp[i - 1] + 1

for i in range(1, n):
    if arr[i] <= arr[i - 1]:
        small_dp[i] = small_dp[i - 1] + 1

print(max(max(big_dp), max(small_dp)))
