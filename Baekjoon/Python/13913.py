from collections import deque


def bfs(N, K):
    Q = deque()
    Q.append((N, [N], 0))
    visited[N] = 1

    while Q:
        cur, arr, cnt = Q.popleft()

        if cur == K:
            return arr

        if cur * 2 <= 10**5 and not visited[cur * 2]:
            Q.append((cur * 2, arr + [cur * 2], cnt + 1))
            visited[cur * 2] = 1
        if cur + 1 <= 10**5 and not visited[cur + 1]:
            Q.append((cur + 1, arr + [cur + 1], cnt + 1))
            visited[cur + 1] = 1
        if cur - 1 >= 0 and not visited[cur - 1]:
            Q.append((cur - 1, arr + [cur - 1], cnt + 1))
            visited[cur - 1] = 1


N, K = map(int, input().split())
visited = [0] * (10**5 + 1)
reverse = 0

if N > K:
    answer = [i for i in range(N, K - 1, -1)]
else:
    answer = bfs(N, K)

print(len(answer) - 1)
print(*answer)
