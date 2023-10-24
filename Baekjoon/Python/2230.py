import sys

input = sys.stdin.readline

N, M = map(int, input().split())

arr = [int(input()) for _ in range(N)]

arr.sort()

s, e = 0, 0
answer = float("inf")

while s < N and e < N:
    temp = arr[e] - arr[s]

    if temp >= M:
        answer = min(answer, temp)
        s += 1
    else:
        e += 1

print(answer)
