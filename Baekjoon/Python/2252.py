import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
inDegree = [0 for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]
queue = deque()
result = []

for _ in range(m):
    a, b = map(int, input().split())

    graph[a].append(b)
    inDegree[b] += 1


for i in range(1, n + 1):
    if inDegree[i] == 0:
        queue.append(i)
        visited[i] = 1

while queue:
    cur = queue.popleft()
    result.append(cur)

    for adj in graph[cur]:
        if visited[adj] == 0:
            inDegree[adj] -= 1
            if visited[adj] == 0 and inDegree[adj] == 0:
                queue.append(adj)
                visited[adj] = 1

print(*result)
