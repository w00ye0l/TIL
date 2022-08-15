from collections import deque
import sys
input = sys.stdin.readline


def bfs(visited, graph, start):
    cnt = 1
    queue.append(start)
    visited[start] = cnt

    while queue:
        cur = queue.popleft()

        for adj in graph[cur]:
            if not visited[adj]:
                queue.append(adj)
                cnt += 1
                visited[adj] = cnt


n, m, r = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
queue = deque()

for _ in range(m):
    u, v = map(int, input().split())

    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n + 1):
    graph[i].sort()

bfs(visited, graph, r)

for i in range(1, n + 1):
    print(visited[i])
