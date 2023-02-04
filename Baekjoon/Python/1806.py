n, s = map(int, input().split())

nums = list(map(int, input().split()))

start, end = 0, 0
sum_ = nums[0]
answer = n + 1

while True:
    if sum_ >= s:
        answer = min(answer, end - start + 1)
        sum_ -= nums[start]
        start += 1
    else:
        end += 1
        if end == n:
            break
        sum_ += nums[end]

print(answer if answer != n + 1 else 0)
