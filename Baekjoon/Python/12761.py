from collections import deque


def bfs(x):
    global answer

    Q = deque()
    Q.append(x)
    visited[x] = 0

    while Q:
        x = Q.popleft()

        if x == M:
            answer = visited[x]
            return

        for n in [-1, -A, -B, 1, A, B]:
            nx = x + n

            if 0 <= nx <= 10**5:
                if visited[nx] != -1:
                    continue

                visited[nx] = visited[x] + 1
                Q.append(nx)

        for n in [A, B]:
            nx = x * n

            if 0 <= nx <= 10**5:
                if visited[nx] != -1:
                    continue

                visited[nx] = visited[x] + 1
                Q.append(nx)


A, B, N, M = map(int, input().split())
answer = 0
visited = [-1 for _ in range(10**5 + 1)]

bfs(N)

print(answer)
