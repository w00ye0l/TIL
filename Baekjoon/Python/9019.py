from collections import deque


def oper_d(n):
    if n * 2 > 9999:
        return (n * 2) % 10000
    else:
        return (n * 2)


def oper_s(n):
    if n - 1 < 0:
        return 9999
    else:
        return (n - 1)


def oper_l(n):
    f = n % 1000
    b = n // 1000

    return (f * 10) + b


def oper_r(n):
    f = n % 10
    b = n // 10

    return (f * 1000) + b


def bfs(s, t):
    queue = deque()
    visited = set()

    queue.append((s, ''))
    visited.add(s)

    while queue:
        cur, oper = queue.popleft()

        if cur == t:
            return oper

        tmp = oper_d(cur)
        if tmp not in visited:
            visited.add(tmp)
            queue.append((tmp, oper + 'D'))

        tmp = oper_s(cur)
        if tmp not in visited:
            visited.add(tmp)
            queue.append((tmp, oper + 'S'))

        tmp = oper_l(cur)
        if tmp not in visited:
            visited.add(tmp)
            queue.append((tmp, oper + 'L'))

        tmp = oper_r(cur)
        if tmp not in visited:
            visited.add(tmp)
            queue.append((tmp, oper + 'R'))


t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    print(bfs(a, b))
