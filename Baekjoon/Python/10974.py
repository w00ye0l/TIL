def dfs():
    if len(nums) == n:
        print(*nums)
        return

    for i in range(1, n + 1):
        if i not in nums:
            nums.append(i)
            dfs()
            nums.pop()


n = int(input())
nums = []
dfs()
