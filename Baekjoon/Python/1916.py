import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize


def dijkstra(start):
    cost[start] = 0
    heap = []
    heapq.heappush(heap, [0, start])

    while heap:
        weight, now = heapq.heappop(heap)

        if cost[now] < weight:
            continue

        for adj, adj_weight in graph[now]:
            new_weight = weight + adj_weight

            if cost[adj] > new_weight:
                cost[adj] = new_weight
                heapq.heappush(heap, [new_weight, adj])


n = int(input())

graph = [[] for _ in range(n + 1)]
cost = [INF for _ in range(n + 1)]

m = int(input())

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

x, y = map(int, input().split())

dijkstra(x)

print(cost[y])
