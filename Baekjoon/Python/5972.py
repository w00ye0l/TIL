import sys
import heapq

input = sys.stdin.readline

def dijkstra():
    queue = []
    distance[1] = 0
    heapq.heappush(queue, (distance[1], 1))

    while queue:
        dis, cur = heapq.heappop(queue)

        if distance[cur] < dis:
            continue

        for adj, adj_dis in graph[cur]:
            if distance[adj] > adj_dis + dis:
                distance[adj] = adj_dis + dis
                heapq.heappush(queue, (adj_dis + dis, adj))


n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
distance = [float("inf") for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())

    graph[a].append((b, c))
    graph[b].append((a, c))

dijkstra()

print(distance[n])
