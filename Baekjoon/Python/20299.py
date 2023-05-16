import sys

input = sys.stdin.readline

N, K, L = map(int, input().split())

cnt = 0
answer = []

for _ in range(N):
    arr = list(map(int, input().split()))
    flag = True

    if sum(arr) < K:
        continue

    for i in range(3):
        if arr[i] < L:
            flag = False
            break

    if flag:
        cnt += 1
        answer.extend(arr)

print(cnt)
print(*answer)
