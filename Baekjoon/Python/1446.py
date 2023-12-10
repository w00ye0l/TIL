import sys
from heapq import heappush, heappop

input = sys.stdin.readline


def dijkstra():
    Q = []
    heappush(Q, (0, 0))
    distance[0] = 0

    while Q:
        dis, now = heappop(Q)

        if dis > distance[now]:
            continue

        for adj, c in graph[now]:
            if dis + c < distance[adj]:
                distance[adj] = dis + c
                heappush(Q, (dis + c, adj))


N, D = map(int, input().split())
graph = [[] for _ in range(D + 1)]
distance = [float("inf")] * (D + 1)

for i in range(D):
    graph[i].append((i + 1, 1))

for i in range(N):
    s, e, d = map(int, input().split())

    if e > D:
        continue

    graph[s].append((e, d))

dijkstra()

print(distance[D])
