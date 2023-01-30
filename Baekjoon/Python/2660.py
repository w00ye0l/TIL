import sys
import heapq

INF = sys.maxsize


def bfs(i):
    visited[i][0] = 0
    visited[i][i] = 0
    heap = []
    heapq.heappush(heap, (0, i))

    while heap:
        dis, cur = heapq.heappop(heap)

        for adj in graph[cur]:
            if visited[i][adj] > dis + 1:
                visited[i][adj] = dis + 1
                heapq.heappush(heap, (visited[i][adj], adj))

    return max(visited[i])


n = int(input())

graph = [[] for _ in range(n + 1)]
visited = [[INF for _ in range(n + 1)] for _ in range(n + 1)]

while True:
    u, v = map(int, input().split())

    if u == -1 and v == -1:
        break

    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n + 1):
    bfs(i)

min_ = min(map(max, visited))

result = []
for i in range(1, n + 1):
    if max(visited[i]) == min_:
        result.append(i)

print(min_, len(result))
print(*result)
