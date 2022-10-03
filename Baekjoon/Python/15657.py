from itertools import combinations_with_replacement

n, m = map(int, input().split())

num = list(map(int, input().split()))
num.sort()

result = list(combinations_with_replacement(num, m))

for r in sorted(result):
    print(*r)
