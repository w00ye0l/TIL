import sys
from collections import defaultdict

trees = defaultdict(int)
cnt = 0

for line in sys.stdin:
    trees[line.rstrip()] += 1
    cnt += 1

trees = sorted(trees.items(), key=lambda x: x[0])

for tree in trees:
    print(f"{tree[0]} {tree[1] / cnt * 100:.4f}")
