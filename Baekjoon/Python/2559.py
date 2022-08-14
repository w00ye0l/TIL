n, k = map(int, input().split())

nums = list(map(int, input().split()))

sum_ = sum(nums[:k])
max_ = sum_

for i in range(n - k):
    sum_ -= nums[i]
    sum_ += nums[i + k]

    if max_ < sum_:
        max_ = sum_

print(max_)
