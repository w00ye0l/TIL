from collections import deque

N, K = map(int, input().split())
arr = deque(map(int, input().split()))
visited = deque([0] * (2 * N))
answer = 0

while arr.count(0) < K:
    answer += 1

    # 1.
    arr.rotate()
    visited.rotate()
    visited[N - 1] = 0

    # 2.
    for i in range(N - 2, -1, -1):
        if arr[i + 1] and visited[i] and not visited[i + 1]:
            arr[i + 1] -= 1
            visited[i + 1], visited[i] = 1, 0
    visited[-1] = 0

    # 3.
    if arr[0] and not visited[0]:
        arr[0] -= 1
        visited[0] = 1

print(answer)
