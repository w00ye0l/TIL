from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
inDegree = [0 for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]
queue = deque()
result = []

for _ in range(m):
    temp = list(map(int, input().split()))

    l = temp[0]
    order = temp[1:]

    for i in range(l):
        for j in range(i + 1, l):
            graph[order[i]].append(order[j])
            inDegree[order[j]] += 1

for i in range(1, n + 1):
    if inDegree[i] == 0:
        queue.append(i)
        visited[i] = 1

while queue:
    cur = queue.popleft()
    result.append(cur)

    for adj in graph[cur]:
        if visited[adj]:
            continue

        inDegree[adj] -= 1
        if inDegree[adj] == 0:
            queue.append(adj)
            visited[adj] = 1

if sum(visited) == n:
    print(*result, sep="\n")
else:
    print(0)
