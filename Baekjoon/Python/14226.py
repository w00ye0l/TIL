from collections import deque

s = int(input())


def bfs(now, clipboard, time):
    queue = deque()
    queue.append((now, clipboard, time))
    visited = [[0] * (s + 1) for _ in range(s + 1)]

    while queue:
        n, c, t = queue.popleft()

        if n == s:
            return t

        if c != 0 and n + c <= s:
            if visited[n + c][c] == 0:
                visited[n + c][c] = 1
                queue.append((n + c, c, t + 1))

        if n > c and visited[n][n] == 0:
            visited[n][n] = 1
            queue.append((n, n, t + 1))

        if n > 1 and visited[n - 1][c] == 0:
            visited[n - 1][c] = 1
            queue.append((n - 1, c, t + 1))


print(bfs(1, 0, 0))
