import sys
from collections import deque

input = sys.stdin.readline
INF = sys.maxsize


def bfs(i, x):
    visited = [INF for _ in range(n + 1)]

    queue = deque()
    queue.append((i, 0))
    visited[i] = 0

    while queue:
        cur, dis = queue.popleft()

        for adj in graph[cur]:
            if visited[adj[0]] > dis + adj[1]:
                visited[adj[0]] = dis + adj[1]
                queue.append((adj[0], dis + adj[1]))

    return visited[x]


n, m, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))


answer = 0

for i in range(1, n + 1):
    temp = bfs(i, x) + bfs(x, i)

    answer = max(answer, temp)

print(answer)
