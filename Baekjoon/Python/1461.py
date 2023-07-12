N, M = map(int, input().split())

arr = list(map(int, input().split())) + [0]

arr.sort()
idx = 0

for i in range(N + 1):
    if arr[i] == 0:
        idx = i

answer = 0

for i in range(0, idx, M):
    answer += abs(arr[i]) * 2

for i in range(N, idx, -M):
    answer += arr[i] * 2

answer -= max(abs(arr[0]), arr[-1])

print(answer)
