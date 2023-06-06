from itertools import product

N, K = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort(reverse=True)
l = len(str(N))
answer = 0

for i in range(l - 1, l + 1):
    for c in product(nums, repeat=i):
        c = int("".join(map(str, c)))
        if c <= N:
            answer = max(answer, c)

print(answer)
