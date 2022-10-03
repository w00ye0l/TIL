from itertools import product

n, m = map(int, input().split())

num = [i for i in range(1, n + 1)]

result = list(product(num, repeat=m))

for r in result:
    print(*r)
