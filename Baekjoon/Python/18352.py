import sys
from collections import deque

input = sys.stdin.readline

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [-1 for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)


def bfs(x):
    queue = deque()
    queue.append(x)
    visited[x] = 0

    while queue:
        cur = queue.popleft()
        for adj in graph[cur]:
            if visited[adj] == -1:
                visited[adj] = visited[cur] + 1
                queue.append(adj)


bfs(x)

if visited.count(k):
    for i in range(1, n + 1):
        if visited[i] == k:
            print(i)
else:
    print(-1)
