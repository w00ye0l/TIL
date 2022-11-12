from itertools import permutations

n, m = map(int, input().split())

num = [i for i in range(1, n + 1)]

for arr in permutations(num, m):
    print(*arr)
