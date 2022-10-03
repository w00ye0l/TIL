from collections import deque


def bfs(i):
    queue = deque()
    queue.append(i)
    visited[i] = 0

    while queue:
        x = queue.popleft()

        if x == 100:
            print(visited[x])
            return

        for k in range(1, 7):
            nx = x + k

            if nx <= 100:
                if nx in ladder:
                    nx = ladder[nx]

                if nx in snake:
                    nx = snake[nx]

                if visited[nx] == -1:
                    visited[nx] = visited[x] + 1
                    queue.append(nx)


n, m = map(int, input().split())
visited = [-1 for _ in range(101)]

ladder = {}
snake = {}
for _ in range(n):
    x, y = map(int, input().split())
    ladder[x] = y

for _ in range(m):
    u, v = map(int, input().split())
    snake[u] = v

bfs(1)
print(visited)
