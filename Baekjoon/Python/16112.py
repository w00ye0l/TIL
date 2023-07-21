n, k = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()

answer = 0
cnt = 0

for i in range(n):
    answer += arr[i] * cnt

    if cnt < k:
        cnt += 1

print(answer)
