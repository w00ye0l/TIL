import sys

input = sys.stdin.readline

n = int(input())

rank = []
for _ in range(n):
    rank.append(int(input()))

rank.sort()

sum_ = 0
for i in range(n):
    sum_ += abs(rank[i] - (i + 1))

print(sum_)
