import sys

input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))

max_ = arr[-1]
cnt = 1
for i in range(n - 2, -1, -1):
    if arr[i] > max_:
        cnt += 1
        max_ = arr[i]

print(cnt)
