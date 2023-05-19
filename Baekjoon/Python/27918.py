import sys

input = sys.stdin.readline

N = int(input())

d, p = 0, 0

for _ in range(N):
    win = input().rstrip()

    if win == "D":
        d += 1
    elif win == "P":
        p += 1

    if abs(d - p) == 2:
        break

print(f"{d}:{p}")
