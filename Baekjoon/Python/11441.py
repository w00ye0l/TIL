import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())

sum_ = [arr[0]]

for i in range(1, N):
    sum_.append(sum_[-1] + arr[i])

for _ in range(M):
    i, j = map(int, input().split())

    if i > 1:
        print(sum_[j - 1] - sum_[i - 2])
    else:
        print(sum_[j - 1])
