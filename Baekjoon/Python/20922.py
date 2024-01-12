from collections import defaultdict

N, K = map(int, input().split())
arr = list(map(int, input().split()))

cnt = defaultdict(int)
s, e = 0, 0
cnt[arr[s]], cnt[arr[e]] = 1, 1
answer = 0

while s < N - 1:
    if e < N - 1 and cnt[arr[e + 1]] < K:
        e += 1
        cnt[arr[e]] += 1
    else:
        cnt[arr[s]] -= 1
        s += 1

    answer = max(answer, e - s + 1)

print(answer)
