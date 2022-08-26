from collections import deque


def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        if abs(f_x - x) + abs(f_y - y) <= 1000:
            print('happy')
            return

        for i in range(n):
            if not visited[i]:
                nx, ny = store[i]

                if abs(nx - x) + abs(ny - y) <= 1000:
                    q.append((nx, ny))
                    visited[i] = 1

    print('sad')
    return


t = int(input())

for _ in range(t):
    n = int(input())
    result = True

    x, y = map(int, input().split())

    store = []
    for _ in range(n):
        u, v = map(int, input().split())
        store.append((u, v))

    f_x, f_y = map(int, input().split())

    visited = [0] * n

    bfs(x, y)
