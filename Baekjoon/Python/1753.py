import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

V, E = map(int, input().split())
K = int(input())

dp = [INF for _ in range(V + 1)]
heap = []
graph = [[] for _ in range(V + 1)]


def dijkstra(start):
    dp[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        weight, cur = heapq.heappop(heap)

        if dp[cur] < weight:
            continue

        for w, next in graph[cur]:
            next_w = weight + w

            if next_w < dp[next]:
                dp[next] = next_w
                heapq.heappush(heap, (next_w, next))


for _ in range(E):
    u, v, w = map(int, input().split())

    graph[u].append((w, v))

dijkstra(K)

for i in range(1, V + 1):
    if dp[i] == INF:
        print("INF")
    else:
        print(dp[i])
