import sys
from collections import deque

input = sys.stdin.readline


def bfs(start, find):
    queue = deque()
    queue.append((start, 0))
    visited = [False] * (n + 1)
    visited[start] = True
    while queue:
        cur, d = queue.popleft()

        if cur == find:
            return d

        for adj, l in graph[cur]:
            if not visited[adj]:
                visited[adj] = True
                queue.append((adj, d + l))


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v, l = map(int, input().split())
    graph[u].append((v, l))
    graph[v].append((u, l))

for _ in range(m):
    u, v = map(int, input().split())
    print(bfs(u, v))
