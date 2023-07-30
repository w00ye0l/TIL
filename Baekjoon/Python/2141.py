import sys

input = sys.stdin.readline

N = int(input())

arr = []
total = 0

for _ in range(N):
    x, a = map(int, input().split())

    arr.append((x, a))
    total += a

arr.sort()

p = 0
for i in range(N):
    p += arr[i][1]

    if p >= total / 2:
        answer = arr[i][0]
        break

print(answer)
