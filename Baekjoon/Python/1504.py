import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize


def dijkstra(start, end):
    distance = [INF for _ in range(n + 1)]
    heap = []
    distance[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        weight, cur = heapq.heappop(heap)

        if distance[cur] < weight:
            continue

        for w, adj in graph[cur]:
            nw = w + weight

            if nw < distance[adj]:
                distance[adj] = nw
                heapq.heappush(heap, (nw, adj))

    return distance[end]


n, e = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    heapq.heappush(graph[a], (c, b))
    heapq.heappush(graph[b], (c, a))

v1, v2 = map(int, input().split())


route1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n)
route2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n)

result = min(route1, route2) if min(route1, route2) < INF else -1

print(result)
