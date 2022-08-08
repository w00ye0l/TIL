t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    nums = [str(i) for i in range(n, m + 1)]
    sum_nums = ''.join(nums)

    print(sum_nums.count('0'))
