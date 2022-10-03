from itertools import permutations

n, m = map(int, input().split())

num = list(map(int, input().split()))

result = list(permutations(num, m))

for r in sorted(result):
    print(*r)
