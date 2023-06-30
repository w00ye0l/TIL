def bt(num, nums):
    if len(nums) == N:
        if set(arr) == set(nums):
            print(*nums)
        return

    if num % 3 == 0:
        if num // 3 in arr:
            nums.append(num // 3)
            bt(num // 3, nums)
            nums.pop()

    nums.append(num * 2)
    bt(num * 2, nums)


N = int(input())
arr = list(map(int, input().split()))

for i in range(N):
    start = [arr[i]]
    bt(arr[i], start)
