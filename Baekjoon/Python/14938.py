import sys
from collections import deque

input = sys.stdin.readline
INF = sys.maxsize


def bfs(i):
    queue = deque()
    queue.append((i, 0))
    distance[i] = 0

    while queue:
        cur, now_dis = queue.popleft()

        for adj in graph[cur]:
            if distance[adj[0]] > now_dis + adj[1]:
                queue.append((adj[0], now_dis + adj[1]))
                distance[adj[0]] = now_dis + adj[1]

    return


n, m, r = map(int, input().split())

items = list(map(int, input().split()))

graph = [[] for _ in range(n + 1)]

for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))

answer = 0

for i in range(1, n + 1):
    distance = [INF for _ in range(n + 1)]

    bfs(i)

    temp = 0
    for j in range(1, n + 1):
        if distance[j] <= m:
            temp += items[j - 1]

    answer = max(answer, temp)

print(answer)
