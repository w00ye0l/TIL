import math
import sys

input = sys.stdin.readline


n, b = map(int, input().split())

x, y = [], []
flag = False

for _ in range(n):
    i, j = map(int, input().split())

    x.append(i)
    y.append(j)

p = sum(x)
q = sum(y) - b * n

if p == 0:
    print("EZPZ")
else:
    p, q = abs(p), abs(q)
    g = math.gcd(p, q)

    if q % p == 0:
        print(q // p)
    elif q * p > 0:
        print(f"{q // g}/{p // g}")
    else:
        print(f"-{q // g}/{p // g}")
