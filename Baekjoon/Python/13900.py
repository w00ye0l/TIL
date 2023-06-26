from itertools import accumulate

N = int(input())
nums = list(map(int, input().split()))

answer = 0

arr = list(accumulate(nums))

for i in range(N):
    answer += nums[i] * (arr[-1] - arr[i])

print(answer)
