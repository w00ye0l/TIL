from collections import deque

n, k = map(int, input().split())

visited = [0 for _ in range(100001)]

min_, result = -1, 0


def bfs(n, k):
    global result, min_

    queue = deque()
    queue.append((n, 0))
    visited[n] = 1

    while queue:
        (cur, t) = queue.popleft()
        visited[cur] = 1

        if t > min_ and min_ != -1:
            return

        if min_ == -1 and cur == k:
            min_ = t
            result += 1
        elif min_ != -1 and cur == k:
            result += 1

        if cur * 2 <= 100000 and not visited[cur * 2]:
            queue.append((cur * 2, t + 1))

        if cur + 1 <= 100000 and not visited[cur + 1]:
            queue.append((cur + 1, t + 1))

        if 0 <= cur - 1 and not visited[cur - 1]:
            queue.append((cur - 1, t + 1))


bfs(n, k)

print(min_)
print(result)
