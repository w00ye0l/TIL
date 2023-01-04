import sys

input = sys.stdin.readline

arr = [0] * 1000001
dp = [0] * 1000001

# 1부터 시작
for i in range(1, 1000001):
    j = 1
    while i * j <= 1000000:
        # i의 배수들에 i를 모두 더함
        dp[i * j] += i
        j += 1

    # 누적합 구하기
    arr[i] = arr[i - 1] + dp[i]


t = int(input())

for _ in range(t):
    n = int(input())

    print(arr[n])
