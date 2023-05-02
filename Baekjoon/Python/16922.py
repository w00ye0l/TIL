from collections import defaultdict


def bt(cnt, idx):
    global num

    if cnt == n:
        result[num] += 1
        return

    for i in range(idx, 4):
        num += nums[i]
        bt(cnt + 1, i)
        num -= nums[i]


n = int(input())

nums = [1, 5, 10, 50]
result = defaultdict(int)
num = 0

bt(0, 0)

print(len(result))
