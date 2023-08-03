from collections import deque


def bfs():
    q = deque()
    q.append((A, B))
    visited = [[0] * total for _ in range(total)]
    visited[A][B] = 1

    while q:
        x, y = q.popleft()
        z = total - x - y

        if x == y == z:
            print(1)
            return

        for a, b in (x, y), (y, z), (z, x):
            if a < b:
                b -= a
                a += a
            elif a > b:
                a -= b
                b += b
            else:
                continue

            c = total - a - b

            X = min(a, b, c)
            Y = max(a, b, c)

            if not visited[X][Y]:
                q.append((X, Y))
                visited[X][Y] = 1

    print(0)


A, B, C = map(int, input().split())

total = A + B + C

if total % 3:
    print(0)
else:
    bfs()
