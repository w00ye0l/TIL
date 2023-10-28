import sys

input = sys.stdin.readline

n = int(input())

answer = 0
arr = []
now = 0

for i in range(n):
    x, y = map(int, input().split())
    now = y

    while arr and arr[-1] > now:
        arr.pop()
        answer += 1

    if arr and arr[-1] == now:
        continue

    arr.append(y)

while arr:
    if arr.pop():
        answer += 1

print(answer)
