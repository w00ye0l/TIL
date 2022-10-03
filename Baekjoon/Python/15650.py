from itertools import combinations

n, m = map(int, input().split())

num = [i for i in range(1, n + 1)]

result = sorted(list(combinations(num, m)))

for r in result:
    print(*r)
