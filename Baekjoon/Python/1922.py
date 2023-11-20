import sys
from heapq import heappush, heappop

input = sys.stdin.readline


def prim():
    Q = []
    Q.append((0, 1))

    answer = 0

    while Q:
        cost, now = heappop(Q)

        if visited[now]:
            continue

        visited[now] = 1
        answer += cost

        for c, adj in graph[now]:
            if not visited[adj]:
                heappush(Q, (c, adj))

    return answer


N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(M):
    a, b, c = map(int, input().split())

    graph[a].append((c, b))
    graph[b].append((c, a))

print(prim())
