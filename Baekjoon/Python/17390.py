import sys

input = sys.stdin.readline

N, Q = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
sum_ = [0] * N

for i in range(N):
    sum_[i] = arr[i] + sum_[i - 1]

for _ in range(Q):
    L, R = map(int, input().split())

    if L == 1:
        print(sum_[R - 1])
    else:
        print(sum_[R - 1] - sum_[L - 2])
