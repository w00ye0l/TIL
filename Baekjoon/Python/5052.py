import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input().rstrip())
    result = 1

    nums = []
    for _ in range(n):
        nums.append(input().rstrip())

    nums.sort()

    for i in range(n - 1):
        if nums[i + 1].startswith(nums[i]):
            result = 0

    if result == 0:
        print('NO')
    else:
        print('YES')
