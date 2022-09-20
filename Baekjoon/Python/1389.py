from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
cnt = [0 for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())

    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n + 1):
    visited = [0 for _ in range(n + 1)]
    queue = deque()

    queue.append(i)
    visited[i] = 1

    while queue:
        cur = queue.popleft()

        for adj in graph[cur]:
            if visited[adj] == 0:
                visited[adj] = visited[cur] + 1
                queue.append(adj)

    cnt[i] = sum(visited)

cnt = cnt[1:]
print(cnt.index(min(cnt)) + 1)
