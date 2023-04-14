import sys

input = sys.stdin.readline

n, k = map(int, input().split())

score = [float(input()) for _ in range(n)]

score.sort()

if k == 0:
    trimmedMean = sum(score) / n + 0.00000001
else:
    trimmedMean = sum(score[k:-k]) / (n - 2 * k) + 0.00000001
print(f"{trimmedMean:.2f}")

for i in range(k):
    score[i], score[-(i + 1)] = score[k], score[-(k + 1)]

adjustedMean = sum(score) / n + 0.00000001
print(f"{adjustedMean:.2f}")
