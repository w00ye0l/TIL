while True:
    n, *nums = map(int, input().split())
    result = []

    if n == 0:
        break

    for i in range(n):
        if len(result) == 0 or result[-1] != nums[i]:
            result.append(nums[i])

    print(" ".join(map(str, result)) + " $")
