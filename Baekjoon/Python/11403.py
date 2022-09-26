from collections import deque

n = int(input())

graph = [[] for _ in range(n)]
for i in range(n):
    temp = list(map(int, input().split()))

    for j in range(n):
        if temp[j] == 1:
            graph[i].append(j)

visited = [[0 for _ in range(n)] for _ in range(n)]

queue = deque()
for i in range(n):
    queue.append(i)

    while queue:
        cur = queue.popleft()

        for adj in graph[cur]:
            if not visited[i][adj]:
                visited[i][adj] = 1
                queue.append(adj)

for v in visited:
    print(*v)
