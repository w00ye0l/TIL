N, K = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

s, e = 0, N - 1
cnt = 0

while s < e:
    if arr[e] >= K:
        e -= 1
    elif arr[s] == K:
        s += 1
    elif arr[s] + arr[e] <= K:
        cnt += 1
        s += 1
        e -= 1
    else:
        e -= 1

print(cnt)
