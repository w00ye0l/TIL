import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())

files = defaultdict(int)

for _ in range(N):
    name, extension = input().rstrip().split(".")

    files[extension] += 1

files = sorted(files.items(), key=lambda x: x[0])

for f in files:
    print(*f)
