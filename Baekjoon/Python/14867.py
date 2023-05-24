from collections import deque

a, b, c, d = map(int, input().split())

Q = deque()
S = set()
answer = -1
Q.append((0, 0, 0))
S.add((0, 0))

while Q:
    cnt, x, y = Q.popleft()

    if x == c and y == d:
        answer = cnt
        break

    if not (a, y) in S:
        Q.append((cnt + 1, a, y))
        S.add((a, y))

    if not (x, b) in S:
        Q.append((cnt + 1, x, b))
        S.add((x, b))

    if not (0, y) in S:
        Q.append((cnt + 1, 0, y))
        S.add((0, y))

    if not (x, 0) in S:
        Q.append((cnt + 1, x, 0))
        S.add((x, 0))

    nx = 0 if b > x + y else x - (b - y)
    ny = x + y if b > x + y else b
    if not (nx, ny) in S:
        Q.append((cnt + 1, nx, ny))
        S.add((nx, ny))

    nx = x + y if a > x + y else a
    ny = 0 if a > x + y else y - (a - x)
    if not (nx, ny) in S:
        Q.append((cnt + 1, nx, ny))
        S.add((nx, ny))

print(answer)
