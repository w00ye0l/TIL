import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())

balloon = defaultdict(int)

for _ in range(N):
    x, y = map(int, input().split())
    sign, d = 0, 0

    if x > 0 and y > 0:
        sign = 1
    elif x < 0 and y > 0:
        sign = 2
    elif x < 0 and y < 0:
        sign = 3
    elif x > 0 and y < 0:
        sign = 4
    elif x > 0 and y == 0:
        sign = 5
    elif x == 0 and y > 0:
        sign = 6
    elif x < 0 and y == 0:
        sign = 7
    elif x == 0 and y < 0:
        sign = 8

    if y == 0:
        d = float("inf")
    else:
        d = x / y

    balloon[(sign, d)] += 1

balloon = sorted(balloon.values(), key=lambda x: -x)

print(balloon[0])
