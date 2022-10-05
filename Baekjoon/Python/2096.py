import sys
from copy import deepcopy

input = sys.stdin.readline

n = int(input())

max_dp = list(map(int, input().split()))
min_dp = deepcopy(max_dp)

for _ in range(1, n):
    num = list(map(int, input().split()))

    max_dp = [
        max(max_dp[0], max_dp[1]) + num[0],
        max(max_dp) + num[1],
        max(max_dp[1], max_dp[2]) + num[2],
    ]

    min_dp = [
        min(min_dp[0], min_dp[1]) + num[0],
        min(min_dp) + num[1],
        min(min_dp[1], min_dp[2]) + num[2],
    ]

print(max(max_dp), min(min_dp))
