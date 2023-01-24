import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())

    graph[a].append((b, c))

start, end = map(int, input().split())


def bfs(i, j):
    heap = []
    heapq.heappush(heap, (i, 0))
    costs = [[INF, []] for _ in range(n + 1)]
    costs[i][0] = 0
    costs[i][1].append(i)

    while heap:
        (cur, cost) = heapq.heappop(heap)

        if costs[cur][0] < cost:
            continue

        for adj, n_cost in graph[cur]:
            if costs[adj][0] > cost + n_cost:
                heapq.heappush(
                    heap,
                    (adj, cost + n_cost),
                )
                costs[adj][0] = cost + n_cost
                costs[adj][1] = costs[cur][1] + [adj]

    return costs[j]


result = bfs(start, end)

print(result[0])
print(len(result[1]))
print(*result[1])
