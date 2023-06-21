N, K = map(int, input().split())
arr = list(map(int, input().split()))
ryan = []
answer = N

for i in range(N):
    if arr[i] == 1:
        ryan.append(i)

if len(ryan) < K:
    print(-1)
else:
    for i in range(len(ryan) - K + 1):
        answer = min(answer, ryan[i + K - 1] - ryan[i] + 1)

    print(answer)
