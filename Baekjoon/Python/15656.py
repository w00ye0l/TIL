from itertools import product

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

print("\n".join(list(map(" ".join, product(map(str, arr), repeat=M)))))
