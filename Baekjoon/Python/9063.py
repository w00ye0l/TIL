import sys

input = sys.stdin.readline

N = int(input())

min_x, min_y, max_x, max_y = 10001, 10001, -10001, -10001

for _ in range(N):
    x, y = map(int, input().split())

    min_x = min(min_x, x)
    max_x = max(max_x, x)
    min_y = min(min_y, y)
    max_y = max(max_y, y)

print((max_x - min_x) * (max_y - min_y))
