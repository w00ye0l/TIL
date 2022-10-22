import sys
from collections import deque

input = sys.stdin.readline


def bfs(start):
    queue = deque()
    queue.append((start, 0))
    visited = [0 for __ in range(10001)]
    visited[start] = 1
    max_dis = 0
    target = 0

    while queue:
        cur, cur_d = queue.popleft()

        for adj, adj_d in graph[cur]:
            if visited[adj]:
                continue

            visited[adj] = 1
            dis = cur_d + adj_d
            if dis > max_dis:
                target, max_dis = adj, dis

            queue.append((adj, dis))
        print(queue, target, max_dis)
    return (target, max_dis)


list_ = []
max_ = 0
while True:
    try:
        start, end, dis = map(int, input().split())
        if max_ < max(start, end):
            max_ = max(start, end)
        list_.append((start, end, dis))
    except:
        break

graph = {i: [] for i in range(10001)}

for l in list_:
    (start, end, dis) = l
    graph[start].append((end, dis))
    graph[end].append((start, dis))

print(bfs(bfs(1)[0])[1])


import sys

input = sys.stdin.readline
from collections import deque


def bfs(start):
    q = deque()
    q.append((start, 0))
    visited = [False for __ in range(10001)]
    visited[start] = True
    max_dist = 0
    target_node = 0
    while q:
        cur_node, cur_dist = q.popleft()
        for next_node, next_dist in graph[cur_node]:
            if visited[next_node]:
                continue
            visited[next_node] = True
            dist = next_dist + cur_dist
            if dist > max_dist:
                max_dist, target_node = dist, next_node
            q.append((next_node, dist))
        print(q, target_node, max_dist)
    return (target_node, max_dist)


edges = []
while 1:
    try:
        a, b, c = map(int, input().split())
        edges.append((a, b, c))
    except:
        break
n = len(edges)
graph = {i: [] for i in range(10001)}
for edge in edges:
    a, b, c = edge
    graph[a].append((b, c))
    graph[b].append((a, c))
print(bfs(bfs(1)[0])[1])
