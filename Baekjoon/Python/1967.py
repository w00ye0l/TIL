import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)


def dfs(n, c):
    for adj in graph[n]:
        (next_node, next_len) = adj
        if distance[next_node] == -1:
            distance[next_node] = c + next_len
            dfs(next_node, c + next_len)


n = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v, d = map(int, input().split())

    graph[u].append((v, d))
    graph[v].append((u, d))

# print(graph)

distance = [-1 for _ in range(n + 1)]
distance[1] = 0
dfs(1, 0)

start = distance.index(max(distance))
distance = [-1 for _ in range(n + 1)]
distance[start] = 0
dfs(start, 0)

print(max(distance))
