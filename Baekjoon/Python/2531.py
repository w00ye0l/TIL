import sys

input = sys.stdin.readline

N, d, k, c = map(int, input().split())

arr = [int(input()) for _ in range(N)]
answer = 0

for s in range(N):
    e = s + k
    visited = set()

    for i in range(s, e):
        i %= N
        visited.add(arr[i])

    cnt = len(visited)
    if not c in visited:
        cnt += 1

    answer = max(answer, cnt)

print(answer)
