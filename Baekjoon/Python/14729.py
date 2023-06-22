import sys

input = sys.stdin.readline

N = int(input())

score = []

for _ in range(N):
    score.append(float(input()))

score.sort()

for i in range(7):
    print(f"{score[i]:.3f}")
