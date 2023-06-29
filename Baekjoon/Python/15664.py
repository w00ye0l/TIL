from itertools import combinations

N, M = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

coms = list(set(combinations(arr, M)))

coms.sort()

for c in coms:
    print(*c)
